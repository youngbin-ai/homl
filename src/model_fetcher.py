from sklearn import ensemble
from sklearn import tree
from sklearn.linear_model import LinearRegression


def get_model(model_name, random_state=42):
    return {
        "linear_regression": LinearRegression(),
        "decision_tree_gini": tree.DecisionTreeClassifier(
            criterion="gini",
            random_state=random_state
        ),
        "decision_tree_entrophy": tree.DecisionTreeClassifier(
            criterion="entrophy",
            random_state=random_state
        ),
        "rf": ensemble.RandomForestClassifier(random_state=random_state),
    }[model_name]