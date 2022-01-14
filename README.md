# calculator_ros_noetic
Robosys_thema2

---
# 概要

[WritingPublisherSubscriber(python)](http://wiki.ros.org/ja/ROS/Tutorials/WritingPublisherSubscriber%28python%29)を元に作成．

## 動画
- 画像をクリックするとYoutubeで動画が再生されます
[![動画](https://user-images.githubusercontent.com/71487860/149426317-0c19dbd5-fc1d-4286-90d2-dac8fe5d45b6.png)](https://youtu.be/myb7oyhUnPA)


**talker**に入力した式を**listener**がeval関数を使って計算し，結果を出力する．
ただし、たまに計算をしてくれないことがある。

---
# バージョン
- ubuntu
  - 20.04.1 LTS

- ROS
  - Noetic

- Python
  - 3.8.5

---
# ビルド

  ```
  $ cd ~/catkin_ws/src
  $ git clone "https://github.com/NaokiIwasawa/calculator_ros_noetic.git"
  $ cd ~/catkin_ws
  $ catkin_make
  $ source ~/.bashrc
  $ cd src/calculator_ros_noetic/scripts
  $ chmod +x talker.py
  $ chmod +x listener.py
  ```
    
---
# 実行

```
terminal1:
$ roscore

terminal2:
$ rosrun calculator talker.py

terminal3:
$ rosrun calculator listener.py
```
# License
[BSD 3-Clause "New" or "Revised" License]("URL")
