> "What would you say if I told you there is an app on the ma-" -Jian Yang

# Hotdog-not-Hotdog-ML

Repo for the ML model that classifies whether an image is a hotdog or not.
This model is a CNN built with TensorFlow.

# Motivation

We built this app for our Grade 12 Computer Science (ICS4U) class. This was a unique project as I was able to use Python for the course (which made the ML 100x easier :P). This is obviously a clone of SeeFood, a fictional app built by Jian Yang. The video is here:

[![Thumbnail](https://i3.ytimg.com/vi/vIci3C4JkL0/maxresdefault.jpg)](https://www.youtube.com/watch?v=vIci3C4JkL0&ab_channel=vietanhle)

## Dataset

The dataset was provided by _yasserhessein_, _Yashvardhan Jain_, and _tanliheng_ from kaggle, the links are: [here](https://www.kaggle.com/yasserhessein/hotdogornothotdog-dataset), [here](https://www.kaggle.com/yashvrdnjain/hotdognothotdog), and [here](https://www.kaggle.com/tanliheng/hot-dog).

```txt
dataset
│
└───train
│   │
│   └───hot_dog
│   │   │   file111.png
│   │   │   file112.png
│   │   │   ...
│   │
│   └───not_hot_dog
│       │   file111.png
│       │   file112.png
│       │   ...
│
└───test
│   │
│   └───hot_dog
│   │   │   file111.png
│   │   │   file112.png
│   │   │   ...
│   │
│   └───not_hot_dog
│       │   file111.png
│       │   file112.png
│       │   ...
│
```

- 2866 images each of hotdogs and not hotdogs in the `train` directory
- 714 images each of hotdogs and not hotdogs in the `test` directory

# Credits

Connor Wilson built the frontend with Java and I built the ML model with Python.
