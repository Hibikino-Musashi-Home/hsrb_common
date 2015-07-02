#!/usr/bin/env python
# vim: fileencoding=utf-8 :
from nose.tools import eq_, ok_, raises
import subprocess
import glob
import os
import tempfile
try:
    import xml.etree.cElementTree as etree
except:
    import xml.etree.ElementTree as etree
from urdf_parser_py.urdf import URDF



PACKAGE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROBOTS_DIR = os.path.join(PACKAGE_DIR, "robots")
URDF_DIR = os.path.join(PACKAGE_DIR, "urdf")


def test_generator_robot_urdf():
    def test_robot_urdf(path):
        u"""XACROで変換した後に、URDFとして正しく読めるかを確認するテスト"""
        with tempfile.NamedTemporaryFile() as f:
            args = ['rosrun', 'xacro', 'xacro.py', source]
            eq_(subprocess.call(args, stdout=f), 0)
            args = ['check_urdf', f.name]
            subprocess.check_output(args)

    matched = glob.glob(ROBOTS_DIR + "/*.urdf.xacro")
    sources = [os.path.abspath(path) for path in matched]
    for source in sources:
        yield test_robot_urdf, source


def test_generator_integrity():
    def check_integrity(source):
        args = ['rosrun', 'xacro', 'xacro.py', source]
        urdf = subprocess.check_output(args)
        root = etree.fromstring(urdf)

        links = []
        for link in root.findall('link'):
            name = link.get('name')
            ok_(name is not None, "link({0})".format(name))
            links.append(name)

        joints = []
        for joint in root.findall('joint'):
            name = joint.get('name')
            ok_(name is not None, "joint({0})".format(name))
            joints.append(name)
            parent = joint.find('parent')
            ok_(parent.get('link') in links, "joint({0})".format(name))
            child = joint.find('child')
            ok_(child.get('link') in links, "joint({0})".format(name))

        for trans in root.findall('transmission'):
            name = trans.get('name')
            joint = trans.find('joint')
            ok_(joint.get('name') in joints, "transmission({0})".format(name))

        for gazebo in root.findall('gazebo'):
            ref = gazebo.get('reference')
            if ref is None:
                # When reference is None, <gazebo> tag is added to <robot>.
                continue
            ok_(ref in links + joints,
                "Unresolvable reference '{0}':\n{1}".format(ref, etree.tostring(gazebo)))

    matched = glob.glob(ROBOTS_DIR + "/*.urdf.xacro")
    sources = [os.path.abspath(path) for path in matched]
    for source in sources:
        yield check_integrity, source
