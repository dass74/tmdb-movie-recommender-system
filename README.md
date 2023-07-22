# tmdb-movie-recommender-system-dass74

This project aims to recommend similar movies for the user using machine learning techniques.

## Overview

This project focuses on two aspects of movie recommendation:

1. **Top Picks for You**: Recommend the top 3 similar movies of the user selected movie.

2. **You Might Also Like**: Recommend the 3 other quite similar movies of the user selected movie.

The project leverages machine learning algorithms to analyze TMDb top 5000 movies data to recommend similar movies for the user.

## Dataset

The project utilizes a dataset comprising movies details such as movie title, overview, rating, cast and crew members etc. The dataset is obtained from reliable sources such as Kaggle. Preprocessing and feature engineering are performed on the dataset to make it suitable for model training and evaluation.

## Technology Stack

The following technologies and tools are used in this project:

- Python: The primary programming language for data preprocessing, model training, and prediction.
- Machine Learning Libraries: Scikit-learn and lightgbm for implementing machine learning models.
- Streamlit: A Python library used to build interactive web applications for showcasing the predictions and results.
- Pandas: Data manipulation and analysis library for preprocessing the dataset.
- NLTK: Python library for working with human language data and text processing tasks.
- Jupyter Notebook: Used for exploratory data analysis and prototyping ML models.

## Usage

To run the TMDb Movie Recommender System:

1. Install the required dependencies listed in `requirements.txt` using `pip install -r requirements.txt`.

2. Import the datasets for training: `tmdb_5000_credits.csv` and `tmdb_5000_movies.csv`.

3. Train the machine learning models on the preprocessed dataset using the provided Jupyter Notebook.

4. Once the models are trained, run the Streamlit application to interactively predict scores and winning teams: `streamlit run app.py`.

## Future Enhancements

There are several areas for further improvement and expansion of this project:

- Developing the full fledged website like TMDb or IMDb where a user can get all the movie details including cast and crew members details.
- Develeoping a smart feature where if a user click on any movie's poster then it will automatically recommend similar movies like that.
- Integrating Web Series and Anime recommendations as well for the user.

## Contributing

Contributions to this project are welcome. Feel free to open issues or submit pull requests with any enhancements, bug fixes, or new features.