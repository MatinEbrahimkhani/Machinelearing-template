import argparse
from src import data_loader, preprocess, train, evaluate, save_load, utils


def main(data_path, model_type, target_column, model_save_path):
    # Ensure directories
    utils.ensure_dir('models')

    # Load data
    df = data_loader.load_data(data_path)

    # Verify columns
    print("Columns in the dataset:", df.columns)

    # Preprocess data
    X_train, X_test, y_train, y_test, preprocessor = preprocess.preprocess_data(df, target_column)

    # Train model
    model = train.train_model(X_train, y_train, model_type)

    # Evaluate model
    metrics = evaluate.evaluate_model(model, X_test, y_test)
    print(f"Evaluation Metrics: {metrics}")

    # Save model and preprocessor
    save_load.save_model(model, model_save_path)
    save_load.save_model(preprocessor, './models/preprocessor.pkl')
    print(f"Model saved to {model_save_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the ML pipeline.")
    parser.add_argument('data_path', type=str, help='Path to the data file.')
    parser.add_argument('model_type', type=str, help='Type of model to train.')
    parser.add_argument('target_column', type=str, help='Target column name.')
    parser.add_argument('model_save_path', type=str, help='Path to save the trained model.')
    args = parser.parse_args()

    main(args.data_path, args.model_type, args.target_column, args.model_save_path)
