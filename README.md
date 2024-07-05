### Predictive Analytics Project: Mildew detection in Cherry Leaves

## Business Requirements

The cherry plantation crop from Farmy & Foods is facing a challenge where their cherry plantations have been presenting powdery mildew. Currently, the process is manual verification if a given cherry tree contains powdery mildew. An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. If there is powdery mildew, the employee applies a specific compound to kill the fungus. The time spent applying this compound is 1 minute. The company has thousands of cherry trees located on multiple farms across the country. As a result, this manual process is not scalable due to the time spent in the manual process inspection.

To save time in this process, the IT team suggested an ML system that detects instantly, using a leaf tree image, if it is healthy or has powdery mildew. A similar manual process is in place for other crops for detecting pests, and if this initiative is successful, there is a realistic chance to replicate this project for all other crops. The dataset is a collection of cherry leaf images provided by Farmy & Foods, taken from their crops.

- 1 - The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.
- 2 - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.

## Dataset Content

- The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves). 
- The dataset contains +4 thousand images taken from the client's crop fields. The images show healthy cherry leaves and cherry leaves that have powdery mildew, a fungal disease that affects many plant species. The cherry plantation crop is one of the finest products in their portfolio, and the company is concerned about supplying the market with a compromised quality product.

## Hypothesis and how to validate?

- We suspect powdery mildew leaves have clear marks/signs, typically on the surface of the leaf, differentiating them from uninfected leaves.
  - An average image study can help to investigate it

## The rationale to map the business requirements to the Data Visualizations and ML tasks

- **Business Requirement 1**: Data Visualization

  - We will display the "mean" and "standard deviation" images for parasitised and uninfected leaves.
  - We will display the difference between average parasitised and uninfected leaves.
  - We will display an image montage for either parasitised or uninfected leaves.

- **Business Requirement 2**: Classification
  - We want to predict if a given leaf is infected or not with powdery mildew.
  - We want to build a binary classifier and generate reports.

## ML Business Case

### PowderyMildewClf

- We want an ML model to predict if a leaf is infected with powdery mildew or not based on historical image data. It is a supervised model, a 2-class, single-label classification model.
- Our ideal outcome is to provide the Farmy & Foods team with a faster and more reliable diagnostic for powdery mildew detection.
- The model success metrics are
  - Accuracy of 65% or above on the test set.
- The model output is defined as a flag, indicating if the leaf has powdery mildew or not and the associated probability of being infected or not. As usual, the Farmy & Foods staff will do the leaves inspection and upload the picture to the App. The prediction is made on the fly (not in batches).
- Heuristics: The current diagnostic needs an experienced staff and detailed inspection to distinguish infected and non-infected leaves. A leaf sample is collected, and examined. Visual criteria are used to detect powdery mildew parasites. It leaves room to produce inaccurate diagnostics due to human error. 
- The training data to fit the model come from the Code Institute team. This dataset contains about 4 thousand images. We have extracted a subset of 4208 images from this dataset and saved it to [Kaggle dataset directory](https://www.kaggle.com/datasets/codeinstitute/cherry-leaves) for quicker model training.
  - Train data - target: infected or not; features: all images.

## Dashboard Design (Streamlit App User Interface)

### Page 1: Quick Project Summary


### Page 2: Leaves Visualiser


### Page 3: Powdery Mildew Detection


### Page 4: Project Hypothesis and Validation


### Page 5: ML Performance Metrics


## Unfixed Bugs

- The application was deployed on [Heroku] (https://cherry-leaves-5-4-67299393f5ab.herokuapp.com/) with limited functionality, because the Heroku platform has a slug limit of 500 MB, so the application was also published on Streamlit with full functionality - https://cherry-leaves-t3-fp7zxkrtcvo8rjsswjcpbz.streamlit.app/. 

## Deployment

### Heroku

- The App live link is: `https://cherry-leaves-5-4-67299393f5ab.herokuapp.com/`
- Set the runtime.txt Python version 3.12.3 to a [Heroku-22](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
- The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click the button Open App on the top of the page to access your App.
6. If the slug size is too large, then add large files not required for the app to the .slugignore file.

## Main Data Analysis and Machine Learning Libraries

- numpy==1.26.4
- pandas==2.2.2
- matplotlib==3.9.0
- seaborn==0.13.2
- plotly==5.22.0
- scikit-learn==1.5.0
- tensorflow-cpu==2.16.1
- keras==3.4.1
- protobuf==4.25.3
- altair==5.3.0

## Credits

- The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves). 
- The dataset contains +4 thousand images taken from the client's crop fields. The images show healthy cherry leaves and cherry leaves that have powdery mildew, a fungal disease that affects many plant species. The cherry plantation crop is one of the finest products in their portfolio, and the company is concerned about supplying the market with a compromised quality product.

### Content

- The text for the Home page was taken from the Code Institute instruction.
- Instructions on how to implement form validation on the Sign-Up page were taken from [Specific YouTube Tutorial](https://www.youtube.com/).


### Media

- The photos dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves).


## Acknowledgements (optional)

- Thanks the Code Institute who provided support throughout this project.

## How to use this repo

1. Use this template to create your GitHub project repo

1. Log into your cloud IDE with your GitHub account.

1. On your Dashboard, click on the New Workspace button

1. Paste in the URL you copied from GitHub earlier

1. Click Create

1. Wait for the workspace to open. This can take a few minutes.

1. Open a new terminal and `pip3 install -r requirements.txt`

1. Open the jupyter_notebooks directory, and click on the notebook you want to open.

1. Click the kernel button and choose Python Environments.

Note that the kernel says Python 3.8.18 as it inherits from the workspace, so it will be Python-3.8.18 as installed by our template. To confirm this, you can use `! python --version` in a notebook code leaf.

## Cloud IDE Reminders

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to _Account Settings_ in the menu under your avatar.
2. Scroll down to the _API Key_ and click _Reveal_
3. Copy the key
4. In the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you, so do not share it. If you accidentally make it public, then you can create a new one with _Regenerate API Key_.
