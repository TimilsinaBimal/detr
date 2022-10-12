# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved
from .detr_multi import build as build_multi
from .detr import build


def build_model(args):
    return build(args)

def build_model_multi(args):
    return build_multi(args)