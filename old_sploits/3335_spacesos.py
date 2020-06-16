#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, re, requests
import string, random, uuid

import time
from concurrent import futures
import grpc
import route_guide_pb2
import route_guide_pb2_grpc
import route_guide_resources


channel = grpc.insecure_channel('localhost:50051')
stub = route_guide_pb2_grpc.RouteGuideStub(channel)

