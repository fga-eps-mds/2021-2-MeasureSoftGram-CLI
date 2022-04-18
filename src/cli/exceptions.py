class MeasureSoftGramCLIException(Exception):
    """Base MeasureSoftGram CLI Exception"""

    pass


class InvalidMetricException(MeasureSoftGramCLIException):
    """Raised when an invalid metric value is provided"""

    pass


class InvalidSonarFileAttributeException(MeasureSoftGramCLIException):
    """Raised when an sonar file attribute is incorrect"""

    pass


class InvalidBaseComponentException(MeasureSoftGramCLIException):
    """Raised when the field baseComponent from sonar metrics file is incorrect"""

    pass


class InvalidFileTypeException(MeasureSoftGramCLIException):
    """' Raised when the file type is not JSON"""

    pass


class MeasureSoftGramCliException(Exception):
    """Base MeasureSoftGram Cli exception"""

    pass


class FileNotFound(MeasureSoftGramCliException):
    """Raised when a invalid file path is provided to the MeasureSoftGram"""

    pass


class NullMetricValue(MeasureSoftGramCliException):
    """Raised when a NULL metric value is provided to the MeasureSoftGram"""

    pass


class InvalidWeightValue(MeasureSoftGramCliException):
    """Raised when a invalid weight value is provided to the MeasureSoftGram"""

    pass


class InvalidCharacteristic(MeasureSoftGramCLIException):
    """Raised when a invalid characteristic is provided to the MeasureSoftGram"""

    pass


class InvalidSubcharacteristic(MeasureSoftGramCLIException):
    """Raised when a invalid subcharacteristic is provided to the MeasureSoftGram"""

    pass


class InvalidMeasure(MeasureSoftGramCLIException):
    """Raised when a invalid measure is provided to the MeasureSoftGram"""

    pass


class InvalidMeasuresoftgramFormat(MeasureSoftGramCLIException):
    """Raised when a invalid format file is provided to the MeasureSoftGram"""

    pass
