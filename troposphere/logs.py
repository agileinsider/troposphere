from . import AWSObject, AWSProperty
from .validators import positive_integer


class LogGroup(AWSObject):
    type = "AWS::Logs::LogGroup"

    props = {
        'RetentionInDays': (positive_integer, False),
    }


class MetricTransformation(AWSProperty):
    props = {
        'MetricName': (basestring, True),
        'MetricNamespace': (basestring, True),
        'MetricValue': (basestring, True),
    }


class MetricFilter(AWSObject):
    type = "AWS::Logs::MetricFilter"

    props = {
        'FilterPattern': ([basestring], True),
        'LogGroupName': (basestring, True),
        'MetricTransformations': ([MetricTransformation], True),
    }
