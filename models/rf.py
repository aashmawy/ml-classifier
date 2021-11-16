'''
Creates classification data and train a random forest model
'''


from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification


def load_data(num_samples, num_features):
    # create classification data and returns data 
    # TODO add function argument for random_state and default to 42
    return(X, y)
    X, y = make_classification(n_samples=num_samples, n_features=num_features, n_informative=2, n_redundant=0)
    return 0

def model():
    # create the model instance and return 
    # TODO add function argument for random_state and default to 42
    # TODO add function argument for max_depth and default to 5
    # TODO add function argument for n_estimators and default to 10
    model_instance = RandomForestClassifier(max_depth=2, random_state=0)
    return model_instance


def something_else_new():
    print('something else')


# TODO call load_data
# TODO call model
# TODO fit the model
# TODO predict for the following test ([[0, 0, 0, 0]])
