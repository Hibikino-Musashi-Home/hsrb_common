本パッケージについて
---------------------------------------
本パッケージはhsrのロボットモデルを管理する。


使用例
---------------------------

次のlaunchを実行することでurdfのロボットモデルがrobot_dsecriptionの名前でパラメータサーバーに、
joint_namesの各軸がjointX/nameの名前でパラメータサーバーに上がる。

    $ roslaunch tmc_hsrb_description upload_beetle.launch

urdfファイルが無いというエラーが出た場合、本パッケージをmakeする。

