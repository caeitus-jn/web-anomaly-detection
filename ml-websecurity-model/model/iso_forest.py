import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split, GridSearchCV, PredefinedSplit
from sklearn.metrics import roc_auc_score, classification_report, make_scorer
import warnings

warnings.filterwarnings('ignore')

normal_df = pd.read_csv('ml-websecurity-model/app/labelled_dataset/normal_log.csv')
mixed_df  = pd.read_csv('ml-websecurity-model/app/labelled_dataset/attack_log.csv')

features = [
    'username_length',
    'password_length',
    'shannon_entropy',
    'contains_SQL',
    'contains_XSS',
    'sql_count',
    'xss_count',
    'no_squotes',
    'no_dquotes'
]

X_mixed = mixed_df[features].values
y_mixed = mixed_df['true_label'].values   

X_val, X_test, y_val, y_test = train_test_split(X_mixed, y_mixed,
                                                test_size = 0.5,
                                                stratify = y_mixed,
                                                random_state = 42
                                                )

X_train_scaled = normal_df[features].values
X_val_scaled   = X_val
X_test_scaled  = X_test


X_hyper = np.vstack([X_train_scaled, X_val_scaled])

y_hyper = np.concatenate([np.zeros(len(X_train_scaled), dtype=int),    
                        (y_val == -1).astype(int)
                        ])

test_fold = np.concatenate([-1 * np.ones(len(X_train_scaled), dtype=int), 
                            0 * np.ones(len(X_val_scaled),   dtype=int)   
                            ])
ps = PredefinedSplit(test_fold)


param_grid = {
    'n_estimators':  [50, 100, 200],
    'max_samples':   [128, 256, 'auto'],
    'contamination': [0.03, 0.06, 0.10, 0.15]
}
scorer = make_scorer(roc_auc_score, needs_threshold=True)

gs = GridSearchCV(
    estimator=IsolationForest(random_state=42),
    param_grid=param_grid,
    scoring=scorer,
    cv=ps,
    n_jobs=-1,
    verbose=1
)
gs.fit(X_hyper, y_hyper)


best = gs.best_params_
final_model = IsolationForest(
    n_estimators=  best['n_estimators'],
    max_samples=   best['max_samples'],
    contamination= best['contamination'],
    random_state=  42
)
final_model.fit(X_train_scaled)

raw_scores    = final_model.decision_function(X_test_scaled)
attack_scores = -raw_scores                      # higher = more likely attack
y_true_attack = (y_test == -1).astype(int)       # attack=1, normal=0

print("Final TEST AUC:", roc_auc_score(y_true_attack, attack_scores))

y_pred        = final_model.predict(X_test_scaled)
y_pred_attack = (y_pred == -1).astype(int)

print(classification_report(
    y_true_attack,
    y_pred_attack,
    target_names=['normal','attack']
))
