from sklearn.ensemble import RandomForestClassifier
import csv_io
import scipy


def main():
    #read in the training file
    train = csv_io.read_data("train.csv")
    
    #set the training responses
    target = [x[0] for x in train]
    
    #set the training features
    train = [x[1,3,4,5,6] for x in train]
    
    #read in the test file
    realtest = csv_io.read_data("test.csv")

    # random forest code
    rf = RandomForestClassifier(n_estimators=10)
    # fit the training data
    print('fitting the model')
    rf.fit(train, target)
    # run model against test data
    predicted_probs = rf.predict_proba(realtest)
        
    predicted_probs = ["%f" % x[1] for x in predicted_probs]
    csv_io.write_delimited_file("random_forest_solution.csv", predicted_probs)


if __name__=="__main__":
    main()