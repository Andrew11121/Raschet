# -*- coding: utf-8 -*-
# @Author: shubhambansal
# @Date:   2018-02-04 23:08:11
# @Last Modified by:   shubhambansal
# @Last Modified time: 2018-02-04 23:25:39
from rest_framework import routers
from part3.viewsets import Part3ViewSet
from part4.viewsets import Part4ViewSet

router = routers.DefaultRouter()

router.register(r'part3', Part3ViewSet)
router.register(r'part4', Part4ViewSet)
