^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package hsrb_description
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

0.12.1 (2016-10-18)
-------------------

0.12.0 (2016-09-26)
-------------------
* fixed wide camera parameters
* Contributors: 村瀬 和都

0.11.1 (2016-08-12)
-------------------
* Modify topic name: depth/points => depth_registered/points
* Contributors: Kazuto Murase

0.11.0 (2016-06-27)
-------------------
* Modify to use OpenNI HW registration
* Contributors: Yuto Mori

0.10.1 (2016-04-12)
-------------------
* change torso damping param to solve torso vibration problem
* fix hand min limit / add comment
* fix hand_motor_joint range
* Contributors: Kazuto Murase, Keisuke Takeshita

0.10.0 (2016-03-14)
-------------------
* change gazebo hardware_interface of base_roll: velocity -> position
* Contributors: Keisuke Takeshita

0.9.1 (2015-11-27)
------------------
* Remove material tag from collision element
* Contributors: 西野 環

0.9.0 (2015-11-23)
------------------
* Fix pointcloud color format to BGR
* Contributors: Akiyoshi Ochiai

0.8.0 (2015-10-22)
------------------
* apply custom grasp_hack plugin
* Contributors: 村瀬 和都

0.7.1 (2015-08-25)
------------------
* fixed wrong links related to wide camera
* Contributors: 村瀬 和都

0.7.0 (2015-08-19)
------------------
* enable hokuyo sensor for intel pc.
* added head_center_gazebo_frame
* use heavier base weight to stabilize move base in gazebo
* Contributors: 寺田　耕志, 村瀬 和都

0.6.0 (2015-07-24)
------------------
* Add visualization switch to laser sensor
* change laser range
* use valid namespace and change sensor config
* add hsrb3 model.
* add hsrb3s
* update inertial and camera size
* Remove unused transmission from hand dummy joints
* changed sensor configuration and grasp hack parameter
* Contributors: Akiyoshi Ochiai, 寺田　耕志, 村瀬 和都

0.5.0 (2015-07-08)
------------------
* Fix camera resolution
* Update RGBD sensor parameter to be compatible with real robots
* use inertial to finger tip frame
* Contributors: Akiyoshi Ochiai, kazuto_murase_aa

0.4.0 (2015-07-03)
------------------
* Add missing test_depend (liburdfdom-tools)
* Merge branch 'feature/fix-invalid-references' of /var/git/repositories/hsr/hsrb_common into develop
* fixed hand_v0 inertial and mass parameters
* Fix joint/link name mismatch
* Add joint/link name integrity test
* Remove unused xacro file
* Update internal reference to old package names
* Change package prefix
* Contributors: Akiyoshi Ochiai, kazuto_murase_aa, 寺田　耕志

0.3.0 (2015-06-11)
------------------
* フレーム/関節/リンク構造の修正
* trajectory駆動のtransmissionをeffortからpositionに変更
* 標準モデルファイルをhsr1sからhsr2sに変更
* mimicのゲイン更新
* 受動輪をキャスターから球に変更
* hokuyoレーザーの角度の分解能を変更
* 関節のtransmission用にhardwareInterfaceタグを追加
* beetle3号機用にモデルファイルを修正
  base,body,laserモデルを新規作成
  すべてのvisualモデルをシェーディング
* collision用mesh修正
* beetle3用にベースのメッシュを変更
* 軽量baseモデルを2Sのbase径に合わせる
* 受動キャスターのtread値を修正
* 受動キャスターを実モデルに追加
* HSR-B2S (Robot No.3) モデルを追加
* UTM-20LXの設定をhokuyoレーザーのentityに追加
* ロボットモデルの軽量化と肩の色を実機に合わせる
* Contributors: 落合 亮吉, 伊豫田 喜美, 田中 和仁, 寺田 耕志

0.2.1 (2014-10-30)
------------------
* cmakeの問題修正
* Contributors: 落合 亮吉

0.2.0 (2014-10-28)
------------------
* depthカメラのtfフレーム修正
* 台車レーザーセンサの色をグレーに
* ハンド関節にダンプパラメータ追加
* URDF生成コマンド修正
* カメラ系のprefixを追加
* センサ群にロボットのネームスペース追加
* ロボットモデルのファイル名変更
* URDFのprefixや関節名を変更
* base_controllerに合うようモデルパラメータ修正
* inertiaテンソルパラメータ修正
* システム要求事項をREADMEに追加
* URDFバリデーションテスト追加
* シミュレータのURDFとメッシュを更新(バージョン毎のレイアウトに)
* tmc_hsrb_simluatorからレポジトリ移動
* Contributors: 落合 亮吉
