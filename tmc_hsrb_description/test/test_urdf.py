#!/usr/bin/env python
# vim: fileencoding=utf-8 :
from nose.tools import eq_
import subprocess
import glob
import os.path
import tempfile


def test_robot_urdf():
    """XACROで変換した後に、URDFとして正しく読めるかを確認するテスト"""
    matched = glob.glob("robots/*.urdf.xacro") + glob.glob("robots/**/*.urdf.xacro")
    sources = [os.path.abspath(path) for path in matched]
    for source in sources:
        args = ['rosrun', 'xacro', 'xacro.py', source]
        with tempfile.NamedTemporaryFile() as f:
            eq_(subprocess.call(args, stdout=f), 0)
            args = ['check_urdf', f.name]
            eq_(subprocess.call(args), 0)
