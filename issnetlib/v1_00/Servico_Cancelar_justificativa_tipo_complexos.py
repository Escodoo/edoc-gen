#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Generated Tue Sep 22 04:41:55 2020 by generateDS.py version 2.36.2.
# Python 3.6.9 (default, Nov  7 2019, 10:44:02)  [GCC 8.3.0]
#
# Command line options:
#   ('--no-collect-includes', '')
#   ('-f', '')
#   ('-o', '/root/generateds/edoc-gen/issnetlib/v1_00/Servico_Cancelar_justificativa_tipo_complexos.py')
#
# Command line arguments:
#   Servico_Cancelar_justificativa_tipo_complexos.xsd
#
# Command line:
#   /root/generateds/generateds-code/generateDS.py --no-collect-includes -f -o "/root/generateds/edoc-gen/issnetlib/v1_00/Servico_Cancelar_justificativa_tipo_complexos.py" Servico_Cancelar_justificativa_tipo_complexos.xsd
#
# Current working directory (os.getcwd()):
#   v1_00
#

from six.moves import zip_longest
import os
import sys
import re as re_
import base64
import datetime as datetime_
import decimal as decimal_
try:
    from lxml import etree as etree_
except ImportError:
    from xml.etree import ElementTree as etree_


Validate_simpletypes_ = True
SaveElementTreeNode = True
if sys.version_info.major == 2:
    BaseStrType_ = basestring
else:
    BaseStrType_ = str


def parsexml_(infile, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        try:
            parser = etree_.ETCompatXMLParser()
        except AttributeError:
            # fallback to xml.etree
            parser = etree_.XMLParser()
    try:
        if isinstance(infile, os.PathLike):
            infile = os.path.join(infile)
    except AttributeError:
        pass
    doc = etree_.parse(infile, parser=parser, **kwargs)
    return doc

def parsexmlstring_(instring, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        try:
            parser = etree_.ETCompatXMLParser()
        except AttributeError:
            # fallback to xml.etree
            parser = etree_.XMLParser()
    element = etree_.fromstring(instring, parser=parser, **kwargs)
    return element

#
# Namespace prefix definition table (and other attributes, too)
#
# The module generatedsnamespaces, if it is importable, must contain
# a dictionary named GeneratedsNamespaceDefs.  This Python dictionary
# should map element type names (strings) to XML schema namespace prefix
# definitions.  The export method for any class for which there is
# a namespace prefix definition, will export that definition in the
# XML representation of that element.  See the export method of
# any generated element type class for an example of the use of this
# table.
# A sample table is:
#
#     # File: generatedsnamespaces.py
#
#     GenerateDSNamespaceDefs = {
#         "ElementtypeA": "http://www.xxx.com/namespaceA",
#         "ElementtypeB": "http://www.xxx.com/namespaceB",
#     }
#
# Additionally, the generatedsnamespaces module can contain a python
# dictionary named GenerateDSNamespaceTypePrefixes that associates element
# types with the namespace prefixes that are to be added to the
# "xsi:type" attribute value.  See the exportAttributes method of
# any generated element type and the generation of "xsi:type" for an
# example of the use of this table.
# An example table:
#
#     # File: generatedsnamespaces.py
#
#     GenerateDSNamespaceTypePrefixes = {
#         "ElementtypeC": "aaa:",
#         "ElementtypeD": "bbb:",
#     }
#

try:
    from generatedsnamespaces import GenerateDSNamespaceDefs as GenerateDSNamespaceDefs_
except ImportError:
    GenerateDSNamespaceDefs_ = {}
try:
    from generatedsnamespaces import GenerateDSNamespaceTypePrefixes as GenerateDSNamespaceTypePrefixes_
except ImportError:
    GenerateDSNamespaceTypePrefixes_ = {}

#
# You can replace the following class definition by defining an
# importable module named "generatedscollector" containing a class
# named "GdsCollector".  See the default class definition below for
# clues about the possible content of that class.
#
try:
    from generatedscollector import GdsCollector as GdsCollector_
except ImportError:

    class GdsCollector_(object):

        def __init__(self, messages=None):
            if messages is None:
                self.messages = []
            else:
                self.messages = messages

        def add_message(self, msg):
            self.messages.append(msg)

        def get_messages(self):
            return self.messages

        def clear_messages(self):
            self.messages = []

        def print_messages(self):
            for msg in self.messages:
                print("Warning: {}".format(msg))

        def write_messages(self, outstream):
            for msg in self.messages:
                outstream.write("Warning: {}\n".format(msg))


#
# The super-class for enum types
#

try:
    from enum import Enum
except ImportError:
    Enum = object

#
# The root super-class for element type classes
#
# Calls to the methods in these classes are generated by generateDS.py.
# You can replace these methods by re-implementing the following class
#   in a module named generatedssuper.py.

try:
    from generatedssuper import GeneratedsSuper
except ImportError as exp:
    
    class GeneratedsSuper(object):
        __hash__ = object.__hash__
        tzoff_pattern = re_.compile(r'(\+|-)((0\d|1[0-3]):[0-5]\d|14:00)$')
        class _FixedOffsetTZ(datetime_.tzinfo):
            def __init__(self, offset, name):
                self.__offset = datetime_.timedelta(minutes=offset)
                self.__name = name
            def utcoffset(self, dt):
                return self.__offset
            def tzname(self, dt):
                return self.__name
            def dst(self, dt):
                return None
        def gds_format_string(self, input_data, input_name=''):
            return input_data
        def gds_parse_string(self, input_data, node=None, input_name=''):
            return input_data
        def gds_validate_string(self, input_data, node=None, input_name=''):
            if not input_data:
                return ''
            else:
                return input_data
        def gds_format_base64(self, input_data, input_name=''):
            return base64.b64encode(input_data)
        def gds_validate_base64(self, input_data, node=None, input_name=''):
            return input_data
        def gds_format_integer(self, input_data, input_name=''):
            return '%d' % input_data
        def gds_parse_integer(self, input_data, node=None, input_name=''):
            try:
                ival = int(input_data)
            except (TypeError, ValueError) as exp:
                raise_parse_error(node, 'Requires integer value: %s' % exp)
            return ival
        def gds_validate_integer(self, input_data, node=None, input_name=''):
            try:
                value = int(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires integer value')
            return value
        def gds_format_integer_list(self, input_data, input_name=''):
            return '%s' % ' '.join(input_data)
        def gds_validate_integer_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    int(value)
                except (TypeError, ValueError):
                    raise_parse_error(node, 'Requires sequence of integer valuess')
            return values
        def gds_format_float(self, input_data, input_name=''):
            return ('%.15f' % input_data).rstrip('0')
        def gds_parse_float(self, input_data, node=None, input_name=''):
            try:
                fval_ = float(input_data)
            except (TypeError, ValueError) as exp:
                raise_parse_error(node, 'Requires float or double value: %s' % exp)
            return fval_
        def gds_validate_float(self, input_data, node=None, input_name=''):
            try:
                value = float(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires float value')
            return value
        def gds_format_float_list(self, input_data, input_name=''):
            return '%s' % ' '.join(input_data)
        def gds_validate_float_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    float(value)
                except (TypeError, ValueError):
                    raise_parse_error(node, 'Requires sequence of float values')
            return values
        def gds_format_decimal(self, input_data, input_name=''):
            return_value = '%s' % input_data
            if '.' in return_value:
                return_value = return_value.rstrip('0')
                if return_value.endswith('.'):
                    return_value = return_value.rstrip('.')
            return return_value
        def gds_parse_decimal(self, input_data, node=None, input_name=''):
            try:
                decimal_value = decimal_.Decimal(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires decimal value')
            return decimal_value
        def gds_validate_decimal(self, input_data, node=None, input_name=''):
            try:
                value = decimal_.Decimal(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires decimal value')
            return value
        def gds_format_decimal_list(self, input_data, input_name=''):
            return ' '.join([self.gds_format_decimal(item) for item in input_data])
        def gds_validate_decimal_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    decimal_.Decimal(value)
                except (TypeError, ValueError):
                    raise_parse_error(node, 'Requires sequence of decimal values')
            return values
        def gds_format_double(self, input_data, input_name=''):
            return '%e' % input_data
        def gds_parse_double(self, input_data, node=None, input_name=''):
            try:
                fval_ = float(input_data)
            except (TypeError, ValueError) as exp:
                raise_parse_error(node, 'Requires double or float value: %s' % exp)
            return fval_
        def gds_validate_double(self, input_data, node=None, input_name=''):
            try:
                value = float(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires double or float value')
            return value
        def gds_format_double_list(self, input_data, input_name=''):
            return '%s' % ' '.join(input_data)
        def gds_validate_double_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    float(value)
                except (TypeError, ValueError):
                    raise_parse_error(
                        node, 'Requires sequence of double or float values')
            return values
        def gds_format_boolean(self, input_data, input_name=''):
            return ('%s' % input_data).lower()
        def gds_parse_boolean(self, input_data, node=None, input_name=''):
            if input_data in ('true', '1'):
                bval = True
            elif input_data in ('false', '0'):
                bval = False
            else:
                raise_parse_error(node, 'Requires boolean value')
            return bval
        def gds_validate_boolean(self, input_data, node=None, input_name=''):
            if input_data not in (True, 1, False, 0, ):
                raise_parse_error(
                    node,
                    'Requires boolean value '
                    '(one of True, 1, False, 0)')
            return input_data
        def gds_format_boolean_list(self, input_data, input_name=''):
            return '%s' % ' '.join(input_data)
        def gds_validate_boolean_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                if value not in (True, 1, False, 0, ):
                    raise_parse_error(
                        node,
                        'Requires sequence of boolean values '
                        '(one of True, 1, False, 0)')
            return values
        def gds_validate_datetime(self, input_data, node=None, input_name=''):
            return input_data
        def gds_format_datetime(self, input_data, input_name=''):
            if input_data.microsecond == 0:
                _svalue = '%04d-%02d-%02dT%02d:%02d:%02d' % (
                    input_data.year,
                    input_data.month,
                    input_data.day,
                    input_data.hour,
                    input_data.minute,
                    input_data.second,
                )
            else:
                _svalue = '%04d-%02d-%02dT%02d:%02d:%02d.%s' % (
                    input_data.year,
                    input_data.month,
                    input_data.day,
                    input_data.hour,
                    input_data.minute,
                    input_data.second,
                    ('%f' % (float(input_data.microsecond) / 1000000))[2:],
                )
            if input_data.tzinfo is not None:
                tzoff = input_data.tzinfo.utcoffset(input_data)
                if tzoff is not None:
                    total_seconds = tzoff.seconds + (86400 * tzoff.days)
                    if total_seconds == 0:
                        _svalue += 'Z'
                    else:
                        if total_seconds < 0:
                            _svalue += '-'
                            total_seconds *= -1
                        else:
                            _svalue += '+'
                        hours = total_seconds // 3600
                        minutes = (total_seconds - (hours * 3600)) // 60
                        _svalue += '{0:02d}:{1:02d}'.format(hours, minutes)
            return _svalue
        @classmethod
        def gds_parse_datetime(cls, input_data):
            tz = None
            if input_data[-1] == 'Z':
                tz = GeneratedsSuper._FixedOffsetTZ(0, 'UTC')
                input_data = input_data[:-1]
            else:
                results = GeneratedsSuper.tzoff_pattern.search(input_data)
                if results is not None:
                    tzoff_parts = results.group(2).split(':')
                    tzoff = int(tzoff_parts[0]) * 60 + int(tzoff_parts[1])
                    if results.group(1) == '-':
                        tzoff *= -1
                    tz = GeneratedsSuper._FixedOffsetTZ(
                        tzoff, results.group(0))
                    input_data = input_data[:-6]
            time_parts = input_data.split('.')
            if len(time_parts) > 1:
                micro_seconds = int(float('0.' + time_parts[1]) * 1000000)
                input_data = '%s.%s' % (
                    time_parts[0], "{}".format(micro_seconds).rjust(6, "0"), )
                dt = datetime_.datetime.strptime(
                    input_data, '%Y-%m-%dT%H:%M:%S.%f')
            else:
                dt = datetime_.datetime.strptime(
                    input_data, '%Y-%m-%dT%H:%M:%S')
            dt = dt.replace(tzinfo=tz)
            return dt
        def gds_validate_date(self, input_data, node=None, input_name=''):
            return input_data
        def gds_format_date(self, input_data, input_name=''):
            _svalue = '%04d-%02d-%02d' % (
                input_data.year,
                input_data.month,
                input_data.day,
            )
            try:
                if input_data.tzinfo is not None:
                    tzoff = input_data.tzinfo.utcoffset(input_data)
                    if tzoff is not None:
                        total_seconds = tzoff.seconds + (86400 * tzoff.days)
                        if total_seconds == 0:
                            _svalue += 'Z'
                        else:
                            if total_seconds < 0:
                                _svalue += '-'
                                total_seconds *= -1
                            else:
                                _svalue += '+'
                            hours = total_seconds // 3600
                            minutes = (total_seconds - (hours * 3600)) // 60
                            _svalue += '{0:02d}:{1:02d}'.format(
                                hours, minutes)
            except AttributeError:
                pass
            return _svalue
        @classmethod
        def gds_parse_date(cls, input_data):
            tz = None
            if input_data[-1] == 'Z':
                tz = GeneratedsSuper._FixedOffsetTZ(0, 'UTC')
                input_data = input_data[:-1]
            else:
                results = GeneratedsSuper.tzoff_pattern.search(input_data)
                if results is not None:
                    tzoff_parts = results.group(2).split(':')
                    tzoff = int(tzoff_parts[0]) * 60 + int(tzoff_parts[1])
                    if results.group(1) == '-':
                        tzoff *= -1
                    tz = GeneratedsSuper._FixedOffsetTZ(
                        tzoff, results.group(0))
                    input_data = input_data[:-6]
            dt = datetime_.datetime.strptime(input_data, '%Y-%m-%d')
            dt = dt.replace(tzinfo=tz)
            return dt.date()
        def gds_validate_time(self, input_data, node=None, input_name=''):
            return input_data
        def gds_format_time(self, input_data, input_name=''):
            if input_data.microsecond == 0:
                _svalue = '%02d:%02d:%02d' % (
                    input_data.hour,
                    input_data.minute,
                    input_data.second,
                )
            else:
                _svalue = '%02d:%02d:%02d.%s' % (
                    input_data.hour,
                    input_data.minute,
                    input_data.second,
                    ('%f' % (float(input_data.microsecond) / 1000000))[2:],
                )
            if input_data.tzinfo is not None:
                tzoff = input_data.tzinfo.utcoffset(input_data)
                if tzoff is not None:
                    total_seconds = tzoff.seconds + (86400 * tzoff.days)
                    if total_seconds == 0:
                        _svalue += 'Z'
                    else:
                        if total_seconds < 0:
                            _svalue += '-'
                            total_seconds *= -1
                        else:
                            _svalue += '+'
                        hours = total_seconds // 3600
                        minutes = (total_seconds - (hours * 3600)) // 60
                        _svalue += '{0:02d}:{1:02d}'.format(hours, minutes)
            return _svalue
        def gds_validate_simple_patterns(self, patterns, target):
            # pat is a list of lists of strings/patterns.
            # The target value must match at least one of the patterns
            # in order for the test to succeed.
            found1 = True
            for patterns1 in patterns:
                found2 = False
                for patterns2 in patterns1:
                    mo = re_.search(patterns2, target)
                    if mo is not None and len(mo.group(0)) == len(target):
                        found2 = True
                        break
                if not found2:
                    found1 = False
                    break
            return found1
        @classmethod
        def gds_parse_time(cls, input_data):
            tz = None
            if input_data[-1] == 'Z':
                tz = GeneratedsSuper._FixedOffsetTZ(0, 'UTC')
                input_data = input_data[:-1]
            else:
                results = GeneratedsSuper.tzoff_pattern.search(input_data)
                if results is not None:
                    tzoff_parts = results.group(2).split(':')
                    tzoff = int(tzoff_parts[0]) * 60 + int(tzoff_parts[1])
                    if results.group(1) == '-':
                        tzoff *= -1
                    tz = GeneratedsSuper._FixedOffsetTZ(
                        tzoff, results.group(0))
                    input_data = input_data[:-6]
            if len(input_data.split('.')) > 1:
                dt = datetime_.datetime.strptime(input_data, '%H:%M:%S.%f')
            else:
                dt = datetime_.datetime.strptime(input_data, '%H:%M:%S')
            dt = dt.replace(tzinfo=tz)
            return dt.time()
        def gds_check_cardinality_(
                self, value, input_name,
                min_occurs=0, max_occurs=1, required=None):
            if value is None:
                length = 0
            elif isinstance(value, list):
                length = len(value)
            else:
                length = 1
            if required is not None :
                if required and length < 1:
                    self.gds_collector_.add_message(
                        "Required value {}{} is missing".format(
                            input_name, self.gds_get_node_lineno_()))
            if length < min_occurs:
                self.gds_collector_.add_message(
                    "Number of values for {}{} is below "
                    "the minimum allowed, "
                    "expected at least {}, found {}".format(
                        input_name, self.gds_get_node_lineno_(),
                        min_occurs, length))
            elif length > max_occurs:
                self.gds_collector_.add_message(
                    "Number of values for {}{} is above "
                    "the maximum allowed, "
                    "expected at most {}, found {}".format(
                        input_name, self.gds_get_node_lineno_(),
                        max_occurs, length))
        def gds_validate_builtin_ST_(
                self, validator, value, input_name,
                min_occurs=None, max_occurs=None, required=None):
            if value is not None:
                try:
                    validator(value, input_name=input_name)
                except GDSParseError as parse_error:
                    self.gds_collector_.add_message(str(parse_error))
        def gds_validate_defined_ST_(
                self, validator, value, input_name,
                min_occurs=None, max_occurs=None, required=None):
            if value is not None:
                try:
                    validator(value)
                except GDSParseError as parse_error:
                    self.gds_collector_.add_message(str(parse_error))
        def gds_str_lower(self, instring):
            return instring.lower()
        def get_path_(self, node):
            path_list = []
            self.get_path_list_(node, path_list)
            path_list.reverse()
            path = '/'.join(path_list)
            return path
        Tag_strip_pattern_ = re_.compile(r'\{.*\}')
        def get_path_list_(self, node, path_list):
            if node is None:
                return
            tag = GeneratedsSuper.Tag_strip_pattern_.sub('', node.tag)
            if tag:
                path_list.append(tag)
            self.get_path_list_(node.getparent(), path_list)
        def get_class_obj_(self, node, default_class=None):
            class_obj1 = default_class
            if 'xsi' in node.nsmap:
                classname = node.get('{%s}type' % node.nsmap['xsi'])
                if classname is not None:
                    names = classname.split(':')
                    if len(names) == 2:
                        classname = names[1]
                    class_obj2 = globals().get(classname)
                    if class_obj2 is not None:
                        class_obj1 = class_obj2
            return class_obj1
        def gds_build_any(self, node, type_name=None):
            # provide default value in case option --disable-xml is used.
            content = ""
            content = etree_.tostring(node, encoding="unicode")
            return content
        @classmethod
        def gds_reverse_node_mapping(cls, mapping):
            return dict(((v, k) for k, v in mapping.items()))
        @staticmethod
        def gds_encode(instring):
            if sys.version_info.major == 2:
                if ExternalEncoding:
                    encoding = ExternalEncoding
                else:
                    encoding = 'utf-8'
                return instring.encode(encoding)
            else:
                return instring
        @staticmethod
        def convert_unicode(instring):
            if isinstance(instring, str):
                result = quote_xml(instring)
            elif sys.version_info.major == 2 and isinstance(instring, unicode):
                result = quote_xml(instring).encode('utf8')
            else:
                result = GeneratedsSuper.gds_encode(str(instring))
            return result
        def __eq__(self, other):
            def excl_select_objs_(obj):
                return (obj[0] != 'parent_object_' and
                        obj[0] != 'gds_collector_')
            if type(self) != type(other):
                return False
            return all(x == y for x, y in zip_longest(
                filter(excl_select_objs_, self.__dict__.items()),
                filter(excl_select_objs_, other.__dict__.items())))
        def __ne__(self, other):
            return not self.__eq__(other)
        # Django ETL transform hooks.
        def gds_djo_etl_transform(self):
            pass
        def gds_djo_etl_transform_db_obj(self, dbobj):
            pass
        # SQLAlchemy ETL transform hooks.
        def gds_sqa_etl_transform(self):
            return 0, None
        def gds_sqa_etl_transform_db_obj(self, dbobj):
            pass
        def gds_get_node_lineno_(self):
            if (hasattr(self, "gds_elementtree_node_") and
                    self.gds_elementtree_node_ is not None):
                return ' near line {}'.format(
                    self.gds_elementtree_node_.sourceline)
            else:
                return ""
    
    
    def getSubclassFromModule_(module, class_):
        '''Get the subclass of a class from a specific module.'''
        name = class_.__name__ + 'Sub'
        if hasattr(module, name):
            return getattr(module, name)
        else:
            return None


#
# If you have installed IPython you can uncomment and use the following.
# IPython is available from http://ipython.scipy.org/.
#

## from IPython.Shell import IPShellEmbed
## args = ''
## ipshell = IPShellEmbed(args,
##     banner = 'Dropping into IPython',
##     exit_msg = 'Leaving Interpreter, back to program.')

# Then use the following line where and when you want to drop into the
# IPython shell:
#    ipshell('<some message> -- Entering ipshell.\nHit Ctrl-D to exit')

#
# Globals
#

ExternalEncoding = ''
# Set this to false in order to deactivate during export, the use of
# name space prefixes captured from the input document.
UseCapturedNS_ = True
CapturedNsmap_ = {}
Tag_pattern_ = re_.compile(r'({.*})?(.*)')
String_cleanup_pat_ = re_.compile(r"[\n\r\s]+")
Namespace_extract_pat_ = re_.compile(r'{(.*)}(.*)')
CDATA_pattern_ = re_.compile(r"<!\[CDATA\[.*?\]\]>", re_.DOTALL)

# Change this to redirect the generated superclass module to use a
# specific subclass module.
CurrentSubclassModule_ = None

#
# Support/utility functions.
#


def showIndent(outfile, level, pretty_print=True):
    if pretty_print:
        for idx in range(level):
            outfile.write('    ')


def quote_xml(inStr):
    "Escape markup chars, but do not modify CDATA sections."
    if not inStr:
        return ''
    s1 = (isinstance(inStr, BaseStrType_) and inStr or '%s' % inStr)
    s2 = ''
    pos = 0
    matchobjects = CDATA_pattern_.finditer(s1)
    for mo in matchobjects:
        s3 = s1[pos:mo.start()]
        s2 += quote_xml_aux(s3)
        s2 += s1[mo.start():mo.end()]
        pos = mo.end()
    s3 = s1[pos:]
    s2 += quote_xml_aux(s3)
    return s2


def quote_xml_aux(inStr):
    s1 = inStr.replace('&', '&amp;')
    s1 = s1.replace('<', '&lt;')
    s1 = s1.replace('>', '&gt;')
    return s1


def quote_attrib(inStr):
    s1 = (isinstance(inStr, BaseStrType_) and inStr or '%s' % inStr)
    s1 = s1.replace('&', '&amp;')
    s1 = s1.replace('<', '&lt;')
    s1 = s1.replace('>', '&gt;')
    if '"' in s1:
        if "'" in s1:
            s1 = '"%s"' % s1.replace('"', "&quot;")
        else:
            s1 = "'%s'" % s1
    else:
        s1 = '"%s"' % s1
    return s1


def quote_python(inStr):
    s1 = inStr
    if s1.find("'") == -1:
        if s1.find('\n') == -1:
            return "'%s'" % s1
        else:
            return "'''%s'''" % s1
    else:
        if s1.find('"') != -1:
            s1 = s1.replace('"', '\\"')
        if s1.find('\n') == -1:
            return '"%s"' % s1
        else:
            return '"""%s"""' % s1


def get_all_text_(node):
    if node.text is not None:
        text = node.text
    else:
        text = ''
    for child in node:
        if child.tail is not None:
            text += child.tail
    return text


def find_attr_value_(attr_name, node):
    attrs = node.attrib
    attr_parts = attr_name.split(':')
    value = None
    if len(attr_parts) == 1:
        value = attrs.get(attr_name)
    elif len(attr_parts) == 2:
        prefix, name = attr_parts
        namespace = node.nsmap.get(prefix)
        if namespace is not None:
            value = attrs.get('{%s}%s' % (namespace, name, ))
    return value


def encode_str_2_3(instr):
    return instr


class GDSParseError(Exception):
    pass


def raise_parse_error(node, msg):
    if node is not None:
        msg = '%s (element %s/line %d)' % (msg, node.tag, node.sourceline, )
    raise GDSParseError(msg)


class MixedContainer:
    # Constants for category:
    CategoryNone = 0
    CategoryText = 1
    CategorySimple = 2
    CategoryComplex = 3
    # Constants for content_type:
    TypeNone = 0
    TypeText = 1
    TypeString = 2
    TypeInteger = 3
    TypeFloat = 4
    TypeDecimal = 5
    TypeDouble = 6
    TypeBoolean = 7
    TypeBase64 = 8
    def __init__(self, category, content_type, name, value):
        self.category = category
        self.content_type = content_type
        self.name = name
        self.value = value
    def getCategory(self):
        return self.category
    def getContenttype(self, content_type):
        return self.content_type
    def getValue(self):
        return self.value
    def getName(self):
        return self.name
    def export(self, outfile, level, name, namespace,
               pretty_print=True):
        if self.category == MixedContainer.CategoryText:
            # Prevent exporting empty content as empty lines.
            if self.value.strip():
                outfile.write(self.value)
        elif self.category == MixedContainer.CategorySimple:
            self.exportSimple(outfile, level, name)
        else:    # category == MixedContainer.CategoryComplex
            self.value.export(
                outfile, level, namespace, name_=name,
                pretty_print=pretty_print)
    def exportSimple(self, outfile, level, name):
        if self.content_type == MixedContainer.TypeString:
            outfile.write('<%s>%s</%s>' % (
                self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeInteger or \
                self.content_type == MixedContainer.TypeBoolean:
            outfile.write('<%s>%d</%s>' % (
                self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeFloat or \
                self.content_type == MixedContainer.TypeDecimal:
            outfile.write('<%s>%f</%s>' % (
                self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeDouble:
            outfile.write('<%s>%g</%s>' % (
                self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeBase64:
            outfile.write('<%s>%s</%s>' % (
                self.name,
                base64.b64encode(self.value),
                self.name))
    def to_etree(self, element, mapping_=None, nsmap_=None):
        if self.category == MixedContainer.CategoryText:
            # Prevent exporting empty content as empty lines.
            if self.value.strip():
                if len(element) > 0:
                    if element[-1].tail is None:
                        element[-1].tail = self.value
                    else:
                        element[-1].tail += self.value
                else:
                    if element.text is None:
                        element.text = self.value
                    else:
                        element.text += self.value
        elif self.category == MixedContainer.CategorySimple:
            subelement = etree_.SubElement(
                element, '%s' % self.name)
            subelement.text = self.to_etree_simple()
        else:    # category == MixedContainer.CategoryComplex
            self.value.to_etree(element)
    def to_etree_simple(self, mapping_=None, nsmap_=None):
        if self.content_type == MixedContainer.TypeString:
            text = self.value
        elif (self.content_type == MixedContainer.TypeInteger or
                self.content_type == MixedContainer.TypeBoolean):
            text = '%d' % self.value
        elif (self.content_type == MixedContainer.TypeFloat or
                self.content_type == MixedContainer.TypeDecimal):
            text = '%f' % self.value
        elif self.content_type == MixedContainer.TypeDouble:
            text = '%g' % self.value
        elif self.content_type == MixedContainer.TypeBase64:
            text = '%s' % base64.b64encode(self.value)
        return text
    def exportLiteral(self, outfile, level, name):
        if self.category == MixedContainer.CategoryText:
            showIndent(outfile, level)
            outfile.write(
                'model_.MixedContainer(%d, %d, "%s", "%s"),\n' % (
                    self.category, self.content_type,
                    self.name, self.value))
        elif self.category == MixedContainer.CategorySimple:
            showIndent(outfile, level)
            outfile.write(
                'model_.MixedContainer(%d, %d, "%s", "%s"),\n' % (
                    self.category, self.content_type,
                    self.name, self.value))
        else:    # category == MixedContainer.CategoryComplex
            showIndent(outfile, level)
            outfile.write(
                'model_.MixedContainer(%d, %d, "%s",\n' % (
                    self.category, self.content_type, self.name,))
            self.value.exportLiteral(outfile, level + 1)
            showIndent(outfile, level)
            outfile.write(')\n')


class MemberSpec_(object):
    def __init__(self, name='', data_type='', container=0,
            optional=0, child_attrs=None, choice=None):
        self.name = name
        self.data_type = data_type
        self.container = container
        self.child_attrs = child_attrs
        self.choice = choice
        self.optional = optional
    def set_name(self, name): self.name = name
    def get_name(self): return self.name
    def set_data_type(self, data_type): self.data_type = data_type
    def get_data_type_chain(self): return self.data_type
    def get_data_type(self):
        if isinstance(self.data_type, list):
            if len(self.data_type) > 0:
                return self.data_type[-1]
            else:
                return 'xs:string'
        else:
            return self.data_type
    def set_container(self, container): self.container = container
    def get_container(self): return self.container
    def set_child_attrs(self, child_attrs): self.child_attrs = child_attrs
    def get_child_attrs(self): return self.child_attrs
    def set_choice(self, choice): self.choice = choice
    def get_choice(self): return self.choice
    def set_optional(self, optional): self.optional = optional
    def get_optional(self): return self.optional


def _cast(typ, value):
    if typ is None or value is None:
        return value
    return typ(value)

#
# Data representation classes.
#


class tcCpfCnpj(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Cpf=None, Cnpj=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Cpf = Cpf
        self.Cpf_nsprefix_ = None
        self.Cnpj = Cnpj
        self.Cnpj_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, tcCpfCnpj)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if tcCpfCnpj.subclass:
            return tcCpfCnpj.subclass(*args_, **kwargs_)
        else:
            return tcCpfCnpj(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Cpf(self):
        return self.Cpf
    def set_Cpf(self, Cpf):
        self.Cpf = Cpf
    def get_Cnpj(self):
        return self.Cnpj
    def set_Cnpj(self, Cnpj):
        self.Cnpj = Cnpj
    def hasContent_(self):
        if (
            self.Cpf is not None or
            self.Cnpj is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:ts="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_simples.xsd" ', name_='tcCpfCnpj', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('tcCpfCnpj')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'tcCpfCnpj':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='tcCpfCnpj')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='tcCpfCnpj', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='tcCpfCnpj'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:ts="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_simples.xsd" ', name_='tcCpfCnpj', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Cpf is not None:
            namespaceprefix_ = self.Cpf_nsprefix_ + ':' if (UseCapturedNS_ and self.Cpf_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCpf>%s</%sCpf>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Cpf), input_name='Cpf')), namespaceprefix_ , eol_))
        if self.Cnpj is not None:
            namespaceprefix_ = self.Cnpj_nsprefix_ + ':' if (UseCapturedNS_ and self.Cnpj_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCnpj>%s</%sCnpj>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Cnpj), input_name='Cnpj')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Cpf':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Cpf')
            value_ = self.gds_validate_string(value_, node, 'Cpf')
            self.Cpf = value_
            self.Cpf_nsprefix_ = child_.prefix
        elif nodeName_ == 'Cnpj':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Cnpj')
            value_ = self.gds_validate_string(value_, node, 'Cnpj')
            self.Cnpj = value_
            self.Cnpj_nsprefix_ = child_.prefix
# end class tcCpfCnpj


class tcEndereco(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Endereco=None, Numero=None, Complemento=None, Bairro=None, Cidade=None, Estado=None, Cep=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Endereco = Endereco
        self.Endereco_nsprefix_ = None
        self.Numero = Numero
        self.Numero_nsprefix_ = None
        self.Complemento = Complemento
        self.Complemento_nsprefix_ = None
        self.Bairro = Bairro
        self.Bairro_nsprefix_ = None
        self.Cidade = Cidade
        self.Cidade_nsprefix_ = None
        self.Estado = Estado
        self.Estado_nsprefix_ = None
        self.Cep = Cep
        self.Cep_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, tcEndereco)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if tcEndereco.subclass:
            return tcEndereco.subclass(*args_, **kwargs_)
        else:
            return tcEndereco(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Endereco(self):
        return self.Endereco
    def set_Endereco(self, Endereco):
        self.Endereco = Endereco
    def get_Numero(self):
        return self.Numero
    def set_Numero(self, Numero):
        self.Numero = Numero
    def get_Complemento(self):
        return self.Complemento
    def set_Complemento(self, Complemento):
        self.Complemento = Complemento
    def get_Bairro(self):
        return self.Bairro
    def set_Bairro(self, Bairro):
        self.Bairro = Bairro
    def get_Cidade(self):
        return self.Cidade
    def set_Cidade(self, Cidade):
        self.Cidade = Cidade
    def get_Estado(self):
        return self.Estado
    def set_Estado(self, Estado):
        self.Estado = Estado
    def get_Cep(self):
        return self.Cep
    def set_Cep(self, Cep):
        self.Cep = Cep
    def hasContent_(self):
        if (
            self.Endereco is not None or
            self.Numero is not None or
            self.Complemento is not None or
            self.Bairro is not None or
            self.Cidade is not None or
            self.Estado is not None or
            self.Cep is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:ts="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_simples.xsd" ', name_='tcEndereco', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('tcEndereco')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'tcEndereco':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='tcEndereco')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='tcEndereco', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='tcEndereco'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:ts="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_simples.xsd" ', name_='tcEndereco', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Endereco is not None:
            namespaceprefix_ = self.Endereco_nsprefix_ + ':' if (UseCapturedNS_ and self.Endereco_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sEndereco>%s</%sEndereco>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Endereco), input_name='Endereco')), namespaceprefix_ , eol_))
        if self.Numero is not None:
            namespaceprefix_ = self.Numero_nsprefix_ + ':' if (UseCapturedNS_ and self.Numero_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sNumero>%s</%sNumero>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Numero), input_name='Numero')), namespaceprefix_ , eol_))
        if self.Complemento is not None:
            namespaceprefix_ = self.Complemento_nsprefix_ + ':' if (UseCapturedNS_ and self.Complemento_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sComplemento>%s</%sComplemento>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Complemento), input_name='Complemento')), namespaceprefix_ , eol_))
        if self.Bairro is not None:
            namespaceprefix_ = self.Bairro_nsprefix_ + ':' if (UseCapturedNS_ and self.Bairro_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sBairro>%s</%sBairro>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Bairro), input_name='Bairro')), namespaceprefix_ , eol_))
        if self.Cidade is not None:
            namespaceprefix_ = self.Cidade_nsprefix_ + ':' if (UseCapturedNS_ and self.Cidade_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCidade>%s</%sCidade>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Cidade), input_name='Cidade')), namespaceprefix_ , eol_))
        if self.Estado is not None:
            namespaceprefix_ = self.Estado_nsprefix_ + ':' if (UseCapturedNS_ and self.Estado_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sEstado>%s</%sEstado>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Estado), input_name='Estado')), namespaceprefix_ , eol_))
        if self.Cep is not None:
            namespaceprefix_ = self.Cep_nsprefix_ + ':' if (UseCapturedNS_ and self.Cep_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCep>%s</%sCep>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Cep), input_name='Cep')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Endereco':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Endereco')
            value_ = self.gds_validate_string(value_, node, 'Endereco')
            self.Endereco = value_
            self.Endereco_nsprefix_ = child_.prefix
        elif nodeName_ == 'Numero':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Numero')
            value_ = self.gds_validate_string(value_, node, 'Numero')
            self.Numero = value_
            self.Numero_nsprefix_ = child_.prefix
        elif nodeName_ == 'Complemento':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Complemento')
            value_ = self.gds_validate_string(value_, node, 'Complemento')
            self.Complemento = value_
            self.Complemento_nsprefix_ = child_.prefix
        elif nodeName_ == 'Bairro':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Bairro')
            value_ = self.gds_validate_string(value_, node, 'Bairro')
            self.Bairro = value_
            self.Bairro_nsprefix_ = child_.prefix
        elif nodeName_ == 'Cidade':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Cidade')
            value_ = self.gds_validate_string(value_, node, 'Cidade')
            self.Cidade = value_
            self.Cidade_nsprefix_ = child_.prefix
        elif nodeName_ == 'Estado':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Estado')
            value_ = self.gds_validate_string(value_, node, 'Estado')
            self.Estado = value_
            self.Estado_nsprefix_ = child_.prefix
        elif nodeName_ == 'Cep':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Cep')
            value_ = self.gds_validate_string(value_, node, 'Cep')
            self.Cep = value_
            self.Cep_nsprefix_ = child_.prefix
# end class tcEndereco


class tcContato(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Telefone=None, Email=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Telefone = Telefone
        self.Telefone_nsprefix_ = None
        self.Email = Email
        self.Email_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, tcContato)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if tcContato.subclass:
            return tcContato.subclass(*args_, **kwargs_)
        else:
            return tcContato(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Telefone(self):
        return self.Telefone
    def set_Telefone(self, Telefone):
        self.Telefone = Telefone
    def get_Email(self):
        return self.Email
    def set_Email(self, Email):
        self.Email = Email
    def hasContent_(self):
        if (
            self.Telefone is not None or
            self.Email is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:ts="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_simples.xsd" ', name_='tcContato', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('tcContato')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'tcContato':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='tcContato')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='tcContato', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='tcContato'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:ts="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_simples.xsd" ', name_='tcContato', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Telefone is not None:
            namespaceprefix_ = self.Telefone_nsprefix_ + ':' if (UseCapturedNS_ and self.Telefone_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sTelefone>%s</%sTelefone>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Telefone), input_name='Telefone')), namespaceprefix_ , eol_))
        if self.Email is not None:
            namespaceprefix_ = self.Email_nsprefix_ + ':' if (UseCapturedNS_ and self.Email_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sEmail>%s</%sEmail>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Email), input_name='Email')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Telefone':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Telefone')
            value_ = self.gds_validate_string(value_, node, 'Telefone')
            self.Telefone = value_
            self.Telefone_nsprefix_ = child_.prefix
        elif nodeName_ == 'Email':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Email')
            value_ = self.gds_validate_string(value_, node, 'Email')
            self.Email = value_
            self.Email_nsprefix_ = child_.prefix
# end class tcContato


class tcIdentificacaoOrgaoGerador(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, CodigoMunicipio=None, Uf=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.CodigoMunicipio = CodigoMunicipio
        self.CodigoMunicipio_nsprefix_ = None
        self.Uf = Uf
        self.Uf_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, tcIdentificacaoOrgaoGerador)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if tcIdentificacaoOrgaoGerador.subclass:
            return tcIdentificacaoOrgaoGerador.subclass(*args_, **kwargs_)
        else:
            return tcIdentificacaoOrgaoGerador(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_CodigoMunicipio(self):
        return self.CodigoMunicipio
    def set_CodigoMunicipio(self, CodigoMunicipio):
        self.CodigoMunicipio = CodigoMunicipio
    def get_Uf(self):
        return self.Uf
    def set_Uf(self, Uf):
        self.Uf = Uf
    def hasContent_(self):
        if (
            self.CodigoMunicipio is not None or
            self.Uf is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:ts="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_simples.xsd" ', name_='tcIdentificacaoOrgaoGerador', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('tcIdentificacaoOrgaoGerador')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'tcIdentificacaoOrgaoGerador':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='tcIdentificacaoOrgaoGerador')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='tcIdentificacaoOrgaoGerador', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='tcIdentificacaoOrgaoGerador'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:ts="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_simples.xsd" ', name_='tcIdentificacaoOrgaoGerador', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.CodigoMunicipio is not None:
            namespaceprefix_ = self.CodigoMunicipio_nsprefix_ + ':' if (UseCapturedNS_ and self.CodigoMunicipio_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCodigoMunicipio>%s</%sCodigoMunicipio>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.CodigoMunicipio), input_name='CodigoMunicipio')), namespaceprefix_ , eol_))
        if self.Uf is not None:
            namespaceprefix_ = self.Uf_nsprefix_ + ':' if (UseCapturedNS_ and self.Uf_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sUf>%s</%sUf>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Uf), input_name='Uf')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'CodigoMunicipio':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'CodigoMunicipio')
            value_ = self.gds_validate_string(value_, node, 'CodigoMunicipio')
            self.CodigoMunicipio = value_
            self.CodigoMunicipio_nsprefix_ = child_.prefix
        elif nodeName_ == 'Uf':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Uf')
            value_ = self.gds_validate_string(value_, node, 'Uf')
            self.Uf = value_
            self.Uf_nsprefix_ = child_.prefix
# end class tcIdentificacaoOrgaoGerador


class tcIdentificacaoRps(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Numero=None, Serie=None, Tipo=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Numero = Numero
        self.Numero_nsprefix_ = None
        self.Serie = Serie
        self.Serie_nsprefix_ = None
        self.Tipo = Tipo
        self.Tipo_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, tcIdentificacaoRps)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if tcIdentificacaoRps.subclass:
            return tcIdentificacaoRps.subclass(*args_, **kwargs_)
        else:
            return tcIdentificacaoRps(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Numero(self):
        return self.Numero
    def set_Numero(self, Numero):
        self.Numero = Numero
    def get_Serie(self):
        return self.Serie
    def set_Serie(self, Serie):
        self.Serie = Serie
    def get_Tipo(self):
        return self.Tipo
    def set_Tipo(self, Tipo):
        self.Tipo = Tipo
    def hasContent_(self):
        if (
            self.Numero is not None or
            self.Serie is not None or
            self.Tipo is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:ts="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_simples.xsd" ', name_='tcIdentificacaoRps', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('tcIdentificacaoRps')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'tcIdentificacaoRps':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='tcIdentificacaoRps')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='tcIdentificacaoRps', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='tcIdentificacaoRps'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:ts="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_simples.xsd" ', name_='tcIdentificacaoRps', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Numero is not None:
            namespaceprefix_ = self.Numero_nsprefix_ + ':' if (UseCapturedNS_ and self.Numero_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sNumero>%s</%sNumero>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Numero), input_name='Numero')), namespaceprefix_ , eol_))
        if self.Serie is not None:
            namespaceprefix_ = self.Serie_nsprefix_ + ':' if (UseCapturedNS_ and self.Serie_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sSerie>%s</%sSerie>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Serie), input_name='Serie')), namespaceprefix_ , eol_))
        if self.Tipo is not None:
            namespaceprefix_ = self.Tipo_nsprefix_ + ':' if (UseCapturedNS_ and self.Tipo_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sTipo>%s</%sTipo>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Tipo), input_name='Tipo')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Numero':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Numero')
            value_ = self.gds_validate_string(value_, node, 'Numero')
            self.Numero = value_
            self.Numero_nsprefix_ = child_.prefix
        elif nodeName_ == 'Serie':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Serie')
            value_ = self.gds_validate_string(value_, node, 'Serie')
            self.Serie = value_
            self.Serie_nsprefix_ = child_.prefix
        elif nodeName_ == 'Tipo':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Tipo')
            value_ = self.gds_validate_string(value_, node, 'Tipo')
            self.Tipo = value_
            self.Tipo_nsprefix_ = child_.prefix
# end class tcIdentificacaoRps


class tcIdentificacaoPrestador(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, CpfCnpj=None, InscricaoMunicipal=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.CpfCnpj = CpfCnpj
        self.CpfCnpj_nsprefix_ = None
        self.InscricaoMunicipal = InscricaoMunicipal
        self.InscricaoMunicipal_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, tcIdentificacaoPrestador)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if tcIdentificacaoPrestador.subclass:
            return tcIdentificacaoPrestador.subclass(*args_, **kwargs_)
        else:
            return tcIdentificacaoPrestador(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_CpfCnpj(self):
        return self.CpfCnpj
    def set_CpfCnpj(self, CpfCnpj):
        self.CpfCnpj = CpfCnpj
    def get_InscricaoMunicipal(self):
        return self.InscricaoMunicipal
    def set_InscricaoMunicipal(self, InscricaoMunicipal):
        self.InscricaoMunicipal = InscricaoMunicipal
    def hasContent_(self):
        if (
            self.CpfCnpj is not None or
            self.InscricaoMunicipal is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd"  xmlns:ts="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_simples.xsd" ', name_='tcIdentificacaoPrestador', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('tcIdentificacaoPrestador')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'tcIdentificacaoPrestador':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='tcIdentificacaoPrestador')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='tcIdentificacaoPrestador', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='tcIdentificacaoPrestador'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd"  xmlns:ts="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_simples.xsd" ', name_='tcIdentificacaoPrestador', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.CpfCnpj is not None:
            namespaceprefix_ = self.CpfCnpj_nsprefix_ + ':' if (UseCapturedNS_ and self.CpfCnpj_nsprefix_) else ''
            self.CpfCnpj.export(outfile, level, namespaceprefix_, namespacedef_='', name_='CpfCnpj', pretty_print=pretty_print)
        if self.InscricaoMunicipal is not None:
            namespaceprefix_ = self.InscricaoMunicipal_nsprefix_ + ':' if (UseCapturedNS_ and self.InscricaoMunicipal_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sInscricaoMunicipal>%s</%sInscricaoMunicipal>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.InscricaoMunicipal), input_name='InscricaoMunicipal')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'CpfCnpj':
            obj_ = tcCpfCnpj.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.CpfCnpj = obj_
            obj_.original_tagname_ = 'CpfCnpj'
        elif nodeName_ == 'InscricaoMunicipal':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'InscricaoMunicipal')
            value_ = self.gds_validate_string(value_, node, 'InscricaoMunicipal')
            self.InscricaoMunicipal = value_
            self.InscricaoMunicipal_nsprefix_ = child_.prefix
# end class tcIdentificacaoPrestador


class tcIdentificacaoTomador(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, CpfCnpj=None, InscricaoMunicipal=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.CpfCnpj = CpfCnpj
        self.CpfCnpj_nsprefix_ = None
        self.InscricaoMunicipal = InscricaoMunicipal
        self.InscricaoMunicipal_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, tcIdentificacaoTomador)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if tcIdentificacaoTomador.subclass:
            return tcIdentificacaoTomador.subclass(*args_, **kwargs_)
        else:
            return tcIdentificacaoTomador(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_CpfCnpj(self):
        return self.CpfCnpj
    def set_CpfCnpj(self, CpfCnpj):
        self.CpfCnpj = CpfCnpj
    def get_InscricaoMunicipal(self):
        return self.InscricaoMunicipal
    def set_InscricaoMunicipal(self, InscricaoMunicipal):
        self.InscricaoMunicipal = InscricaoMunicipal
    def hasContent_(self):
        if (
            self.CpfCnpj is not None or
            self.InscricaoMunicipal is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd"  xmlns:ts="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_simples.xsd" ', name_='tcIdentificacaoTomador', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('tcIdentificacaoTomador')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'tcIdentificacaoTomador':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='tcIdentificacaoTomador')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='tcIdentificacaoTomador', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='tcIdentificacaoTomador'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd"  xmlns:ts="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_simples.xsd" ', name_='tcIdentificacaoTomador', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.CpfCnpj is not None:
            namespaceprefix_ = self.CpfCnpj_nsprefix_ + ':' if (UseCapturedNS_ and self.CpfCnpj_nsprefix_) else ''
            self.CpfCnpj.export(outfile, level, namespaceprefix_, namespacedef_='', name_='CpfCnpj', pretty_print=pretty_print)
        if self.InscricaoMunicipal is not None:
            namespaceprefix_ = self.InscricaoMunicipal_nsprefix_ + ':' if (UseCapturedNS_ and self.InscricaoMunicipal_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sInscricaoMunicipal>%s</%sInscricaoMunicipal>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.InscricaoMunicipal), input_name='InscricaoMunicipal')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'CpfCnpj':
            obj_ = tcCpfCnpj.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.CpfCnpj = obj_
            obj_.original_tagname_ = 'CpfCnpj'
        elif nodeName_ == 'InscricaoMunicipal':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'InscricaoMunicipal')
            value_ = self.gds_validate_string(value_, node, 'InscricaoMunicipal')
            self.InscricaoMunicipal = value_
            self.InscricaoMunicipal_nsprefix_ = child_.prefix
# end class tcIdentificacaoTomador


class tcDadosTomador(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, IdentificacaoTomador=None, RazaoSocial=None, Endereco=None, Contato=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.IdentificacaoTomador = IdentificacaoTomador
        self.IdentificacaoTomador_nsprefix_ = None
        self.RazaoSocial = RazaoSocial
        self.RazaoSocial_nsprefix_ = None
        self.Endereco = Endereco
        self.Endereco_nsprefix_ = None
        self.Contato = Contato
        self.Contato_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, tcDadosTomador)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if tcDadosTomador.subclass:
            return tcDadosTomador.subclass(*args_, **kwargs_)
        else:
            return tcDadosTomador(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_IdentificacaoTomador(self):
        return self.IdentificacaoTomador
    def set_IdentificacaoTomador(self, IdentificacaoTomador):
        self.IdentificacaoTomador = IdentificacaoTomador
    def get_RazaoSocial(self):
        return self.RazaoSocial
    def set_RazaoSocial(self, RazaoSocial):
        self.RazaoSocial = RazaoSocial
    def get_Endereco(self):
        return self.Endereco
    def set_Endereco(self, Endereco):
        self.Endereco = Endereco
    def get_Contato(self):
        return self.Contato
    def set_Contato(self, Contato):
        self.Contato = Contato
    def hasContent_(self):
        if (
            self.IdentificacaoTomador is not None or
            self.RazaoSocial is not None or
            self.Endereco is not None or
            self.Contato is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd"  xmlns:ts="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_simples.xsd" ', name_='tcDadosTomador', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('tcDadosTomador')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'tcDadosTomador':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='tcDadosTomador')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='tcDadosTomador', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='tcDadosTomador'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd"  xmlns:ts="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_simples.xsd" ', name_='tcDadosTomador', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.IdentificacaoTomador is not None:
            namespaceprefix_ = self.IdentificacaoTomador_nsprefix_ + ':' if (UseCapturedNS_ and self.IdentificacaoTomador_nsprefix_) else ''
            self.IdentificacaoTomador.export(outfile, level, namespaceprefix_, namespacedef_='', name_='IdentificacaoTomador', pretty_print=pretty_print)
        if self.RazaoSocial is not None:
            namespaceprefix_ = self.RazaoSocial_nsprefix_ + ':' if (UseCapturedNS_ and self.RazaoSocial_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sRazaoSocial>%s</%sRazaoSocial>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.RazaoSocial), input_name='RazaoSocial')), namespaceprefix_ , eol_))
        if self.Endereco is not None:
            namespaceprefix_ = self.Endereco_nsprefix_ + ':' if (UseCapturedNS_ and self.Endereco_nsprefix_) else ''
            self.Endereco.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Endereco', pretty_print=pretty_print)
        if self.Contato is not None:
            namespaceprefix_ = self.Contato_nsprefix_ + ':' if (UseCapturedNS_ and self.Contato_nsprefix_) else ''
            self.Contato.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Contato', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'IdentificacaoTomador':
            obj_ = tcIdentificacaoTomador.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.IdentificacaoTomador = obj_
            obj_.original_tagname_ = 'IdentificacaoTomador'
        elif nodeName_ == 'RazaoSocial':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'RazaoSocial')
            value_ = self.gds_validate_string(value_, node, 'RazaoSocial')
            self.RazaoSocial = value_
            self.RazaoSocial_nsprefix_ = child_.prefix
        elif nodeName_ == 'Endereco':
            obj_ = tcEndereco.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Endereco = obj_
            obj_.original_tagname_ = 'Endereco'
        elif nodeName_ == 'Contato':
            obj_ = tcContato.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Contato = obj_
            obj_.original_tagname_ = 'Contato'
# end class tcDadosTomador


class tcIdentificacaoIntermediarioServico(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, RazaoSocial=None, CpfCnpj=None, InscricaoMunicipal=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.RazaoSocial = RazaoSocial
        self.RazaoSocial_nsprefix_ = None
        self.CpfCnpj = CpfCnpj
        self.CpfCnpj_nsprefix_ = None
        self.InscricaoMunicipal = InscricaoMunicipal
        self.InscricaoMunicipal_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, tcIdentificacaoIntermediarioServico)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if tcIdentificacaoIntermediarioServico.subclass:
            return tcIdentificacaoIntermediarioServico.subclass(*args_, **kwargs_)
        else:
            return tcIdentificacaoIntermediarioServico(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_RazaoSocial(self):
        return self.RazaoSocial
    def set_RazaoSocial(self, RazaoSocial):
        self.RazaoSocial = RazaoSocial
    def get_CpfCnpj(self):
        return self.CpfCnpj
    def set_CpfCnpj(self, CpfCnpj):
        self.CpfCnpj = CpfCnpj
    def get_InscricaoMunicipal(self):
        return self.InscricaoMunicipal
    def set_InscricaoMunicipal(self, InscricaoMunicipal):
        self.InscricaoMunicipal = InscricaoMunicipal
    def hasContent_(self):
        if (
            self.RazaoSocial is not None or
            self.CpfCnpj is not None or
            self.InscricaoMunicipal is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:ts="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_simples.xsd"  xmlns:None="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd" ', name_='tcIdentificacaoIntermediarioServico', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('tcIdentificacaoIntermediarioServico')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'tcIdentificacaoIntermediarioServico':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='tcIdentificacaoIntermediarioServico')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='tcIdentificacaoIntermediarioServico', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='tcIdentificacaoIntermediarioServico'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:ts="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_simples.xsd"  xmlns:None="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd" ', name_='tcIdentificacaoIntermediarioServico', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.RazaoSocial is not None:
            namespaceprefix_ = self.RazaoSocial_nsprefix_ + ':' if (UseCapturedNS_ and self.RazaoSocial_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sRazaoSocial>%s</%sRazaoSocial>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.RazaoSocial), input_name='RazaoSocial')), namespaceprefix_ , eol_))
        if self.CpfCnpj is not None:
            namespaceprefix_ = self.CpfCnpj_nsprefix_ + ':' if (UseCapturedNS_ and self.CpfCnpj_nsprefix_) else ''
            self.CpfCnpj.export(outfile, level, namespaceprefix_, namespacedef_='', name_='CpfCnpj', pretty_print=pretty_print)
        if self.InscricaoMunicipal is not None:
            namespaceprefix_ = self.InscricaoMunicipal_nsprefix_ + ':' if (UseCapturedNS_ and self.InscricaoMunicipal_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sInscricaoMunicipal>%s</%sInscricaoMunicipal>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.InscricaoMunicipal), input_name='InscricaoMunicipal')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'RazaoSocial':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'RazaoSocial')
            value_ = self.gds_validate_string(value_, node, 'RazaoSocial')
            self.RazaoSocial = value_
            self.RazaoSocial_nsprefix_ = child_.prefix
        elif nodeName_ == 'CpfCnpj':
            obj_ = tcCpfCnpj.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.CpfCnpj = obj_
            obj_.original_tagname_ = 'CpfCnpj'
        elif nodeName_ == 'InscricaoMunicipal':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'InscricaoMunicipal')
            value_ = self.gds_validate_string(value_, node, 'InscricaoMunicipal')
            self.InscricaoMunicipal = value_
            self.InscricaoMunicipal_nsprefix_ = child_.prefix
# end class tcIdentificacaoIntermediarioServico


class tcValores(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, ValorServicos=None, ValorDeducoes=None, ValorPis=None, ValorCofins=None, ValorInss=None, ValorIr=None, ValorCsll=None, IssRetido=None, ValorIss=None, ValorIssRetido=None, OutrasRetencoes=None, BaseCalculo=None, Aliquota=None, ValorLiquidoNfse=None, DescontoIncondicionado=None, DescontoCondicionado=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.ValorServicos = ValorServicos
        self.ValorServicos_nsprefix_ = None
        self.ValorDeducoes = ValorDeducoes
        self.ValorDeducoes_nsprefix_ = None
        self.ValorPis = ValorPis
        self.ValorPis_nsprefix_ = None
        self.ValorCofins = ValorCofins
        self.ValorCofins_nsprefix_ = None
        self.ValorInss = ValorInss
        self.ValorInss_nsprefix_ = None
        self.ValorIr = ValorIr
        self.ValorIr_nsprefix_ = None
        self.ValorCsll = ValorCsll
        self.ValorCsll_nsprefix_ = None
        self.IssRetido = IssRetido
        self.IssRetido_nsprefix_ = None
        self.ValorIss = ValorIss
        self.ValorIss_nsprefix_ = None
        self.ValorIssRetido = ValorIssRetido
        self.ValorIssRetido_nsprefix_ = None
        self.OutrasRetencoes = OutrasRetencoes
        self.OutrasRetencoes_nsprefix_ = None
        self.BaseCalculo = BaseCalculo
        self.BaseCalculo_nsprefix_ = None
        self.Aliquota = Aliquota
        self.Aliquota_nsprefix_ = None
        self.ValorLiquidoNfse = ValorLiquidoNfse
        self.ValorLiquidoNfse_nsprefix_ = None
        self.DescontoIncondicionado = DescontoIncondicionado
        self.DescontoIncondicionado_nsprefix_ = None
        self.DescontoCondicionado = DescontoCondicionado
        self.DescontoCondicionado_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, tcValores)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if tcValores.subclass:
            return tcValores.subclass(*args_, **kwargs_)
        else:
            return tcValores(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_ValorServicos(self):
        return self.ValorServicos
    def set_ValorServicos(self, ValorServicos):
        self.ValorServicos = ValorServicos
    def get_ValorDeducoes(self):
        return self.ValorDeducoes
    def set_ValorDeducoes(self, ValorDeducoes):
        self.ValorDeducoes = ValorDeducoes
    def get_ValorPis(self):
        return self.ValorPis
    def set_ValorPis(self, ValorPis):
        self.ValorPis = ValorPis
    def get_ValorCofins(self):
        return self.ValorCofins
    def set_ValorCofins(self, ValorCofins):
        self.ValorCofins = ValorCofins
    def get_ValorInss(self):
        return self.ValorInss
    def set_ValorInss(self, ValorInss):
        self.ValorInss = ValorInss
    def get_ValorIr(self):
        return self.ValorIr
    def set_ValorIr(self, ValorIr):
        self.ValorIr = ValorIr
    def get_ValorCsll(self):
        return self.ValorCsll
    def set_ValorCsll(self, ValorCsll):
        self.ValorCsll = ValorCsll
    def get_IssRetido(self):
        return self.IssRetido
    def set_IssRetido(self, IssRetido):
        self.IssRetido = IssRetido
    def get_ValorIss(self):
        return self.ValorIss
    def set_ValorIss(self, ValorIss):
        self.ValorIss = ValorIss
    def get_ValorIssRetido(self):
        return self.ValorIssRetido
    def set_ValorIssRetido(self, ValorIssRetido):
        self.ValorIssRetido = ValorIssRetido
    def get_OutrasRetencoes(self):
        return self.OutrasRetencoes
    def set_OutrasRetencoes(self, OutrasRetencoes):
        self.OutrasRetencoes = OutrasRetencoes
    def get_BaseCalculo(self):
        return self.BaseCalculo
    def set_BaseCalculo(self, BaseCalculo):
        self.BaseCalculo = BaseCalculo
    def get_Aliquota(self):
        return self.Aliquota
    def set_Aliquota(self, Aliquota):
        self.Aliquota = Aliquota
    def get_ValorLiquidoNfse(self):
        return self.ValorLiquidoNfse
    def set_ValorLiquidoNfse(self, ValorLiquidoNfse):
        self.ValorLiquidoNfse = ValorLiquidoNfse
    def get_DescontoIncondicionado(self):
        return self.DescontoIncondicionado
    def set_DescontoIncondicionado(self, DescontoIncondicionado):
        self.DescontoIncondicionado = DescontoIncondicionado
    def get_DescontoCondicionado(self):
        return self.DescontoCondicionado
    def set_DescontoCondicionado(self, DescontoCondicionado):
        self.DescontoCondicionado = DescontoCondicionado
    def hasContent_(self):
        if (
            self.ValorServicos is not None or
            self.ValorDeducoes is not None or
            self.ValorPis is not None or
            self.ValorCofins is not None or
            self.ValorInss is not None or
            self.ValorIr is not None or
            self.ValorCsll is not None or
            self.IssRetido is not None or
            self.ValorIss is not None or
            self.ValorIssRetido is not None or
            self.OutrasRetencoes is not None or
            self.BaseCalculo is not None or
            self.Aliquota is not None or
            self.ValorLiquidoNfse is not None or
            self.DescontoIncondicionado is not None or
            self.DescontoCondicionado is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:ts="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_simples.xsd" ', name_='tcValores', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('tcValores')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'tcValores':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='tcValores')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='tcValores', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='tcValores'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:ts="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_simples.xsd" ', name_='tcValores', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.ValorServicos is not None:
            namespaceprefix_ = self.ValorServicos_nsprefix_ + ':' if (UseCapturedNS_ and self.ValorServicos_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sValorServicos>%s</%sValorServicos>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.ValorServicos), input_name='ValorServicos')), namespaceprefix_ , eol_))
        if self.ValorDeducoes is not None:
            namespaceprefix_ = self.ValorDeducoes_nsprefix_ + ':' if (UseCapturedNS_ and self.ValorDeducoes_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sValorDeducoes>%s</%sValorDeducoes>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.ValorDeducoes), input_name='ValorDeducoes')), namespaceprefix_ , eol_))
        if self.ValorPis is not None:
            namespaceprefix_ = self.ValorPis_nsprefix_ + ':' if (UseCapturedNS_ and self.ValorPis_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sValorPis>%s</%sValorPis>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.ValorPis), input_name='ValorPis')), namespaceprefix_ , eol_))
        if self.ValorCofins is not None:
            namespaceprefix_ = self.ValorCofins_nsprefix_ + ':' if (UseCapturedNS_ and self.ValorCofins_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sValorCofins>%s</%sValorCofins>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.ValorCofins), input_name='ValorCofins')), namespaceprefix_ , eol_))
        if self.ValorInss is not None:
            namespaceprefix_ = self.ValorInss_nsprefix_ + ':' if (UseCapturedNS_ and self.ValorInss_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sValorInss>%s</%sValorInss>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.ValorInss), input_name='ValorInss')), namespaceprefix_ , eol_))
        if self.ValorIr is not None:
            namespaceprefix_ = self.ValorIr_nsprefix_ + ':' if (UseCapturedNS_ and self.ValorIr_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sValorIr>%s</%sValorIr>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.ValorIr), input_name='ValorIr')), namespaceprefix_ , eol_))
        if self.ValorCsll is not None:
            namespaceprefix_ = self.ValorCsll_nsprefix_ + ':' if (UseCapturedNS_ and self.ValorCsll_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sValorCsll>%s</%sValorCsll>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.ValorCsll), input_name='ValorCsll')), namespaceprefix_ , eol_))
        if self.IssRetido is not None:
            namespaceprefix_ = self.IssRetido_nsprefix_ + ':' if (UseCapturedNS_ and self.IssRetido_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sIssRetido>%s</%sIssRetido>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.IssRetido), input_name='IssRetido')), namespaceprefix_ , eol_))
        if self.ValorIss is not None:
            namespaceprefix_ = self.ValorIss_nsprefix_ + ':' if (UseCapturedNS_ and self.ValorIss_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sValorIss>%s</%sValorIss>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.ValorIss), input_name='ValorIss')), namespaceprefix_ , eol_))
        if self.ValorIssRetido is not None:
            namespaceprefix_ = self.ValorIssRetido_nsprefix_ + ':' if (UseCapturedNS_ and self.ValorIssRetido_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sValorIssRetido>%s</%sValorIssRetido>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.ValorIssRetido), input_name='ValorIssRetido')), namespaceprefix_ , eol_))
        if self.OutrasRetencoes is not None:
            namespaceprefix_ = self.OutrasRetencoes_nsprefix_ + ':' if (UseCapturedNS_ and self.OutrasRetencoes_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sOutrasRetencoes>%s</%sOutrasRetencoes>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.OutrasRetencoes), input_name='OutrasRetencoes')), namespaceprefix_ , eol_))
        if self.BaseCalculo is not None:
            namespaceprefix_ = self.BaseCalculo_nsprefix_ + ':' if (UseCapturedNS_ and self.BaseCalculo_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sBaseCalculo>%s</%sBaseCalculo>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.BaseCalculo), input_name='BaseCalculo')), namespaceprefix_ , eol_))
        if self.Aliquota is not None:
            namespaceprefix_ = self.Aliquota_nsprefix_ + ':' if (UseCapturedNS_ and self.Aliquota_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sAliquota>%s</%sAliquota>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Aliquota), input_name='Aliquota')), namespaceprefix_ , eol_))
        if self.ValorLiquidoNfse is not None:
            namespaceprefix_ = self.ValorLiquidoNfse_nsprefix_ + ':' if (UseCapturedNS_ and self.ValorLiquidoNfse_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sValorLiquidoNfse>%s</%sValorLiquidoNfse>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.ValorLiquidoNfse), input_name='ValorLiquidoNfse')), namespaceprefix_ , eol_))
        if self.DescontoIncondicionado is not None:
            namespaceprefix_ = self.DescontoIncondicionado_nsprefix_ + ':' if (UseCapturedNS_ and self.DescontoIncondicionado_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sDescontoIncondicionado>%s</%sDescontoIncondicionado>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.DescontoIncondicionado), input_name='DescontoIncondicionado')), namespaceprefix_ , eol_))
        if self.DescontoCondicionado is not None:
            namespaceprefix_ = self.DescontoCondicionado_nsprefix_ + ':' if (UseCapturedNS_ and self.DescontoCondicionado_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sDescontoCondicionado>%s</%sDescontoCondicionado>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.DescontoCondicionado), input_name='DescontoCondicionado')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'ValorServicos':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'ValorServicos')
            value_ = self.gds_validate_string(value_, node, 'ValorServicos')
            self.ValorServicos = value_
            self.ValorServicos_nsprefix_ = child_.prefix
        elif nodeName_ == 'ValorDeducoes':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'ValorDeducoes')
            value_ = self.gds_validate_string(value_, node, 'ValorDeducoes')
            self.ValorDeducoes = value_
            self.ValorDeducoes_nsprefix_ = child_.prefix
        elif nodeName_ == 'ValorPis':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'ValorPis')
            value_ = self.gds_validate_string(value_, node, 'ValorPis')
            self.ValorPis = value_
            self.ValorPis_nsprefix_ = child_.prefix
        elif nodeName_ == 'ValorCofins':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'ValorCofins')
            value_ = self.gds_validate_string(value_, node, 'ValorCofins')
            self.ValorCofins = value_
            self.ValorCofins_nsprefix_ = child_.prefix
        elif nodeName_ == 'ValorInss':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'ValorInss')
            value_ = self.gds_validate_string(value_, node, 'ValorInss')
            self.ValorInss = value_
            self.ValorInss_nsprefix_ = child_.prefix
        elif nodeName_ == 'ValorIr':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'ValorIr')
            value_ = self.gds_validate_string(value_, node, 'ValorIr')
            self.ValorIr = value_
            self.ValorIr_nsprefix_ = child_.prefix
        elif nodeName_ == 'ValorCsll':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'ValorCsll')
            value_ = self.gds_validate_string(value_, node, 'ValorCsll')
            self.ValorCsll = value_
            self.ValorCsll_nsprefix_ = child_.prefix
        elif nodeName_ == 'IssRetido':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'IssRetido')
            value_ = self.gds_validate_string(value_, node, 'IssRetido')
            self.IssRetido = value_
            self.IssRetido_nsprefix_ = child_.prefix
        elif nodeName_ == 'ValorIss':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'ValorIss')
            value_ = self.gds_validate_string(value_, node, 'ValorIss')
            self.ValorIss = value_
            self.ValorIss_nsprefix_ = child_.prefix
        elif nodeName_ == 'ValorIssRetido':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'ValorIssRetido')
            value_ = self.gds_validate_string(value_, node, 'ValorIssRetido')
            self.ValorIssRetido = value_
            self.ValorIssRetido_nsprefix_ = child_.prefix
        elif nodeName_ == 'OutrasRetencoes':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'OutrasRetencoes')
            value_ = self.gds_validate_string(value_, node, 'OutrasRetencoes')
            self.OutrasRetencoes = value_
            self.OutrasRetencoes_nsprefix_ = child_.prefix
        elif nodeName_ == 'BaseCalculo':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'BaseCalculo')
            value_ = self.gds_validate_string(value_, node, 'BaseCalculo')
            self.BaseCalculo = value_
            self.BaseCalculo_nsprefix_ = child_.prefix
        elif nodeName_ == 'Aliquota':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Aliquota')
            value_ = self.gds_validate_string(value_, node, 'Aliquota')
            self.Aliquota = value_
            self.Aliquota_nsprefix_ = child_.prefix
        elif nodeName_ == 'ValorLiquidoNfse':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'ValorLiquidoNfse')
            value_ = self.gds_validate_string(value_, node, 'ValorLiquidoNfse')
            self.ValorLiquidoNfse = value_
            self.ValorLiquidoNfse_nsprefix_ = child_.prefix
        elif nodeName_ == 'DescontoIncondicionado':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'DescontoIncondicionado')
            value_ = self.gds_validate_string(value_, node, 'DescontoIncondicionado')
            self.DescontoIncondicionado = value_
            self.DescontoIncondicionado_nsprefix_ = child_.prefix
        elif nodeName_ == 'DescontoCondicionado':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'DescontoCondicionado')
            value_ = self.gds_validate_string(value_, node, 'DescontoCondicionado')
            self.DescontoCondicionado = value_
            self.DescontoCondicionado_nsprefix_ = child_.prefix
# end class tcValores


class tcDadosServico(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Valores=None, ItemListaServico=None, CodigoCnae=None, CodigoTributacaoMunicipio=None, Discriminacao=None, MunicipioPrestacaoServico=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Valores = Valores
        self.Valores_nsprefix_ = None
        self.ItemListaServico = ItemListaServico
        self.ItemListaServico_nsprefix_ = None
        self.CodigoCnae = CodigoCnae
        self.CodigoCnae_nsprefix_ = None
        self.CodigoTributacaoMunicipio = CodigoTributacaoMunicipio
        self.CodigoTributacaoMunicipio_nsprefix_ = None
        self.Discriminacao = Discriminacao
        self.Discriminacao_nsprefix_ = None
        self.MunicipioPrestacaoServico = MunicipioPrestacaoServico
        self.MunicipioPrestacaoServico_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, tcDadosServico)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if tcDadosServico.subclass:
            return tcDadosServico.subclass(*args_, **kwargs_)
        else:
            return tcDadosServico(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Valores(self):
        return self.Valores
    def set_Valores(self, Valores):
        self.Valores = Valores
    def get_ItemListaServico(self):
        return self.ItemListaServico
    def set_ItemListaServico(self, ItemListaServico):
        self.ItemListaServico = ItemListaServico
    def get_CodigoCnae(self):
        return self.CodigoCnae
    def set_CodigoCnae(self, CodigoCnae):
        self.CodigoCnae = CodigoCnae
    def get_CodigoTributacaoMunicipio(self):
        return self.CodigoTributacaoMunicipio
    def set_CodigoTributacaoMunicipio(self, CodigoTributacaoMunicipio):
        self.CodigoTributacaoMunicipio = CodigoTributacaoMunicipio
    def get_Discriminacao(self):
        return self.Discriminacao
    def set_Discriminacao(self, Discriminacao):
        self.Discriminacao = Discriminacao
    def get_MunicipioPrestacaoServico(self):
        return self.MunicipioPrestacaoServico
    def set_MunicipioPrestacaoServico(self, MunicipioPrestacaoServico):
        self.MunicipioPrestacaoServico = MunicipioPrestacaoServico
    def hasContent_(self):
        if (
            self.Valores is not None or
            self.ItemListaServico is not None or
            self.CodigoCnae is not None or
            self.CodigoTributacaoMunicipio is not None or
            self.Discriminacao is not None or
            self.MunicipioPrestacaoServico is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd"  xmlns:ts="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_simples.xsd" ', name_='tcDadosServico', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('tcDadosServico')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'tcDadosServico':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='tcDadosServico')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='tcDadosServico', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='tcDadosServico'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd"  xmlns:ts="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_simples.xsd" ', name_='tcDadosServico', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Valores is not None:
            namespaceprefix_ = self.Valores_nsprefix_ + ':' if (UseCapturedNS_ and self.Valores_nsprefix_) else ''
            self.Valores.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Valores', pretty_print=pretty_print)
        if self.ItemListaServico is not None:
            namespaceprefix_ = self.ItemListaServico_nsprefix_ + ':' if (UseCapturedNS_ and self.ItemListaServico_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sItemListaServico>%s</%sItemListaServico>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.ItemListaServico), input_name='ItemListaServico')), namespaceprefix_ , eol_))
        if self.CodigoCnae is not None:
            namespaceprefix_ = self.CodigoCnae_nsprefix_ + ':' if (UseCapturedNS_ and self.CodigoCnae_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCodigoCnae>%s</%sCodigoCnae>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.CodigoCnae), input_name='CodigoCnae')), namespaceprefix_ , eol_))
        if self.CodigoTributacaoMunicipio is not None:
            namespaceprefix_ = self.CodigoTributacaoMunicipio_nsprefix_ + ':' if (UseCapturedNS_ and self.CodigoTributacaoMunicipio_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCodigoTributacaoMunicipio>%s</%sCodigoTributacaoMunicipio>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.CodigoTributacaoMunicipio), input_name='CodigoTributacaoMunicipio')), namespaceprefix_ , eol_))
        if self.Discriminacao is not None:
            namespaceprefix_ = self.Discriminacao_nsprefix_ + ':' if (UseCapturedNS_ and self.Discriminacao_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sDiscriminacao>%s</%sDiscriminacao>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Discriminacao), input_name='Discriminacao')), namespaceprefix_ , eol_))
        if self.MunicipioPrestacaoServico is not None:
            namespaceprefix_ = self.MunicipioPrestacaoServico_nsprefix_ + ':' if (UseCapturedNS_ and self.MunicipioPrestacaoServico_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sMunicipioPrestacaoServico>%s</%sMunicipioPrestacaoServico>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.MunicipioPrestacaoServico), input_name='MunicipioPrestacaoServico')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Valores':
            obj_ = tcValores.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Valores = obj_
            obj_.original_tagname_ = 'Valores'
        elif nodeName_ == 'ItemListaServico':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'ItemListaServico')
            value_ = self.gds_validate_string(value_, node, 'ItemListaServico')
            self.ItemListaServico = value_
            self.ItemListaServico_nsprefix_ = child_.prefix
        elif nodeName_ == 'CodigoCnae':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'CodigoCnae')
            value_ = self.gds_validate_string(value_, node, 'CodigoCnae')
            self.CodigoCnae = value_
            self.CodigoCnae_nsprefix_ = child_.prefix
        elif nodeName_ == 'CodigoTributacaoMunicipio':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'CodigoTributacaoMunicipio')
            value_ = self.gds_validate_string(value_, node, 'CodigoTributacaoMunicipio')
            self.CodigoTributacaoMunicipio = value_
            self.CodigoTributacaoMunicipio_nsprefix_ = child_.prefix
        elif nodeName_ == 'Discriminacao':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Discriminacao')
            value_ = self.gds_validate_string(value_, node, 'Discriminacao')
            self.Discriminacao = value_
            self.Discriminacao_nsprefix_ = child_.prefix
        elif nodeName_ == 'MunicipioPrestacaoServico':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'MunicipioPrestacaoServico')
            value_ = self.gds_validate_string(value_, node, 'MunicipioPrestacaoServico')
            self.MunicipioPrestacaoServico = value_
            self.MunicipioPrestacaoServico_nsprefix_ = child_.prefix
# end class tcDadosServico


class tcDadosConstrucaoCivil(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, CodigoObra=None, Art=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.CodigoObra = CodigoObra
        self.CodigoObra_nsprefix_ = None
        self.Art = Art
        self.Art_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, tcDadosConstrucaoCivil)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if tcDadosConstrucaoCivil.subclass:
            return tcDadosConstrucaoCivil.subclass(*args_, **kwargs_)
        else:
            return tcDadosConstrucaoCivil(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_CodigoObra(self):
        return self.CodigoObra
    def set_CodigoObra(self, CodigoObra):
        self.CodigoObra = CodigoObra
    def get_Art(self):
        return self.Art
    def set_Art(self, Art):
        self.Art = Art
    def hasContent_(self):
        if (
            self.CodigoObra is not None or
            self.Art is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:ts="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_simples.xsd" ', name_='tcDadosConstrucaoCivil', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('tcDadosConstrucaoCivil')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'tcDadosConstrucaoCivil':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='tcDadosConstrucaoCivil')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='tcDadosConstrucaoCivil', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='tcDadosConstrucaoCivil'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:ts="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_simples.xsd" ', name_='tcDadosConstrucaoCivil', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.CodigoObra is not None:
            namespaceprefix_ = self.CodigoObra_nsprefix_ + ':' if (UseCapturedNS_ and self.CodigoObra_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCodigoObra>%s</%sCodigoObra>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.CodigoObra), input_name='CodigoObra')), namespaceprefix_ , eol_))
        if self.Art is not None:
            namespaceprefix_ = self.Art_nsprefix_ + ':' if (UseCapturedNS_ and self.Art_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sArt>%s</%sArt>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Art), input_name='Art')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'CodigoObra':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'CodigoObra')
            value_ = self.gds_validate_string(value_, node, 'CodigoObra')
            self.CodigoObra = value_
            self.CodigoObra_nsprefix_ = child_.prefix
        elif nodeName_ == 'Art':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Art')
            value_ = self.gds_validate_string(value_, node, 'Art')
            self.Art = value_
            self.Art_nsprefix_ = child_.prefix
# end class tcDadosConstrucaoCivil


class tcDadosPrestador(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, IdentificacaoPrestador=None, RazaoSocial=None, NomeFantasia=None, Endereco=None, Contato=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.IdentificacaoPrestador = IdentificacaoPrestador
        self.IdentificacaoPrestador_nsprefix_ = None
        self.RazaoSocial = RazaoSocial
        self.RazaoSocial_nsprefix_ = None
        self.NomeFantasia = NomeFantasia
        self.NomeFantasia_nsprefix_ = None
        self.Endereco = Endereco
        self.Endereco_nsprefix_ = None
        self.Contato = Contato
        self.Contato_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, tcDadosPrestador)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if tcDadosPrestador.subclass:
            return tcDadosPrestador.subclass(*args_, **kwargs_)
        else:
            return tcDadosPrestador(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_IdentificacaoPrestador(self):
        return self.IdentificacaoPrestador
    def set_IdentificacaoPrestador(self, IdentificacaoPrestador):
        self.IdentificacaoPrestador = IdentificacaoPrestador
    def get_RazaoSocial(self):
        return self.RazaoSocial
    def set_RazaoSocial(self, RazaoSocial):
        self.RazaoSocial = RazaoSocial
    def get_NomeFantasia(self):
        return self.NomeFantasia
    def set_NomeFantasia(self, NomeFantasia):
        self.NomeFantasia = NomeFantasia
    def get_Endereco(self):
        return self.Endereco
    def set_Endereco(self, Endereco):
        self.Endereco = Endereco
    def get_Contato(self):
        return self.Contato
    def set_Contato(self, Contato):
        self.Contato = Contato
    def hasContent_(self):
        if (
            self.IdentificacaoPrestador is not None or
            self.RazaoSocial is not None or
            self.NomeFantasia is not None or
            self.Endereco is not None or
            self.Contato is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd"  xmlns:ts="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_simples.xsd" ', name_='tcDadosPrestador', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('tcDadosPrestador')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'tcDadosPrestador':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='tcDadosPrestador')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='tcDadosPrestador', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='tcDadosPrestador'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd"  xmlns:ts="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_simples.xsd" ', name_='tcDadosPrestador', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.IdentificacaoPrestador is not None:
            namespaceprefix_ = self.IdentificacaoPrestador_nsprefix_ + ':' if (UseCapturedNS_ and self.IdentificacaoPrestador_nsprefix_) else ''
            self.IdentificacaoPrestador.export(outfile, level, namespaceprefix_, namespacedef_='', name_='IdentificacaoPrestador', pretty_print=pretty_print)
        if self.RazaoSocial is not None:
            namespaceprefix_ = self.RazaoSocial_nsprefix_ + ':' if (UseCapturedNS_ and self.RazaoSocial_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sRazaoSocial>%s</%sRazaoSocial>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.RazaoSocial), input_name='RazaoSocial')), namespaceprefix_ , eol_))
        if self.NomeFantasia is not None:
            namespaceprefix_ = self.NomeFantasia_nsprefix_ + ':' if (UseCapturedNS_ and self.NomeFantasia_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sNomeFantasia>%s</%sNomeFantasia>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.NomeFantasia), input_name='NomeFantasia')), namespaceprefix_ , eol_))
        if self.Endereco is not None:
            namespaceprefix_ = self.Endereco_nsprefix_ + ':' if (UseCapturedNS_ and self.Endereco_nsprefix_) else ''
            self.Endereco.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Endereco', pretty_print=pretty_print)
        if self.Contato is not None:
            namespaceprefix_ = self.Contato_nsprefix_ + ':' if (UseCapturedNS_ and self.Contato_nsprefix_) else ''
            self.Contato.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Contato', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'IdentificacaoPrestador':
            obj_ = tcIdentificacaoPrestador.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.IdentificacaoPrestador = obj_
            obj_.original_tagname_ = 'IdentificacaoPrestador'
        elif nodeName_ == 'RazaoSocial':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'RazaoSocial')
            value_ = self.gds_validate_string(value_, node, 'RazaoSocial')
            self.RazaoSocial = value_
            self.RazaoSocial_nsprefix_ = child_.prefix
        elif nodeName_ == 'NomeFantasia':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'NomeFantasia')
            value_ = self.gds_validate_string(value_, node, 'NomeFantasia')
            self.NomeFantasia = value_
            self.NomeFantasia_nsprefix_ = child_.prefix
        elif nodeName_ == 'Endereco':
            obj_ = tcEndereco.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Endereco = obj_
            obj_.original_tagname_ = 'Endereco'
        elif nodeName_ == 'Contato':
            obj_ = tcContato.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Contato = obj_
            obj_.original_tagname_ = 'Contato'
# end class tcDadosPrestador


class tcAtividade(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, CodigoAtividade=None, DescricaoAtividade=None, Aliquota=None, VigenciaInicial=None, VigenciaFinal=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.CodigoAtividade = CodigoAtividade
        self.CodigoAtividade_nsprefix_ = None
        self.DescricaoAtividade = DescricaoAtividade
        self.DescricaoAtividade_nsprefix_ = None
        self.Aliquota = Aliquota
        self.Aliquota_nsprefix_ = None
        if isinstance(VigenciaInicial, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(VigenciaInicial, '%Y-%m-%d').date()
        else:
            initvalue_ = VigenciaInicial
        self.VigenciaInicial = initvalue_
        self.VigenciaInicial_nsprefix_ = None
        if isinstance(VigenciaFinal, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(VigenciaFinal, '%Y-%m-%d').date()
        else:
            initvalue_ = VigenciaFinal
        self.VigenciaFinal = initvalue_
        self.VigenciaFinal_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, tcAtividade)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if tcAtividade.subclass:
            return tcAtividade.subclass(*args_, **kwargs_)
        else:
            return tcAtividade(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_CodigoAtividade(self):
        return self.CodigoAtividade
    def set_CodigoAtividade(self, CodigoAtividade):
        self.CodigoAtividade = CodigoAtividade
    def get_DescricaoAtividade(self):
        return self.DescricaoAtividade
    def set_DescricaoAtividade(self, DescricaoAtividade):
        self.DescricaoAtividade = DescricaoAtividade
    def get_Aliquota(self):
        return self.Aliquota
    def set_Aliquota(self, Aliquota):
        self.Aliquota = Aliquota
    def get_VigenciaInicial(self):
        return self.VigenciaInicial
    def set_VigenciaInicial(self, VigenciaInicial):
        self.VigenciaInicial = VigenciaInicial
    def get_VigenciaFinal(self):
        return self.VigenciaFinal
    def set_VigenciaFinal(self, VigenciaFinal):
        self.VigenciaFinal = VigenciaFinal
    def hasContent_(self):
        if (
            self.CodigoAtividade is not None or
            self.DescricaoAtividade is not None or
            self.Aliquota is not None or
            self.VigenciaInicial is not None or
            self.VigenciaFinal is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd"  xmlns:ts="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_simples.xsd" ', name_='tcAtividade', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('tcAtividade')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'tcAtividade':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='tcAtividade')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='tcAtividade', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='tcAtividade'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd"  xmlns:ts="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_simples.xsd" ', name_='tcAtividade', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.CodigoAtividade is not None:
            namespaceprefix_ = self.CodigoAtividade_nsprefix_ + ':' if (UseCapturedNS_ and self.CodigoAtividade_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCodigoAtividade>%s</%sCodigoAtividade>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.CodigoAtividade), input_name='CodigoAtividade')), namespaceprefix_ , eol_))
        if self.DescricaoAtividade is not None:
            namespaceprefix_ = self.DescricaoAtividade_nsprefix_ + ':' if (UseCapturedNS_ and self.DescricaoAtividade_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sDescricaoAtividade>%s</%sDescricaoAtividade>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.DescricaoAtividade), input_name='DescricaoAtividade')), namespaceprefix_ , eol_))
        if self.Aliquota is not None:
            namespaceprefix_ = self.Aliquota_nsprefix_ + ':' if (UseCapturedNS_ and self.Aliquota_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sAliquota>%s</%sAliquota>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Aliquota), input_name='Aliquota')), namespaceprefix_ , eol_))
        if self.VigenciaInicial is not None:
            namespaceprefix_ = self.VigenciaInicial_nsprefix_ + ':' if (UseCapturedNS_ and self.VigenciaInicial_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sVigenciaInicial>%s</%sVigenciaInicial>%s' % (namespaceprefix_ , self.gds_format_date(self.VigenciaInicial, input_name='VigenciaInicial'), namespaceprefix_ , eol_))
        if self.VigenciaFinal is not None:
            namespaceprefix_ = self.VigenciaFinal_nsprefix_ + ':' if (UseCapturedNS_ and self.VigenciaFinal_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sVigenciaFinal>%s</%sVigenciaFinal>%s' % (namespaceprefix_ , self.gds_format_date(self.VigenciaFinal, input_name='VigenciaFinal'), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'CodigoAtividade':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'CodigoAtividade')
            value_ = self.gds_validate_string(value_, node, 'CodigoAtividade')
            self.CodigoAtividade = value_
            self.CodigoAtividade_nsprefix_ = child_.prefix
        elif nodeName_ == 'DescricaoAtividade':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'DescricaoAtividade')
            value_ = self.gds_validate_string(value_, node, 'DescricaoAtividade')
            self.DescricaoAtividade = value_
            self.DescricaoAtividade_nsprefix_ = child_.prefix
        elif nodeName_ == 'Aliquota':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Aliquota')
            value_ = self.gds_validate_string(value_, node, 'Aliquota')
            self.Aliquota = value_
            self.Aliquota_nsprefix_ = child_.prefix
        elif nodeName_ == 'VigenciaInicial':
            sval_ = child_.text
            dval_ = self.gds_parse_date(sval_)
            self.VigenciaInicial = dval_
            self.VigenciaInicial_nsprefix_ = child_.prefix
        elif nodeName_ == 'VigenciaFinal':
            sval_ = child_.text
            dval_ = self.gds_parse_date(sval_)
            self.VigenciaFinal = dval_
            self.VigenciaFinal_nsprefix_ = child_.prefix
# end class tcAtividade


class tcSimplesNacional(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, OptanteSimplesNacional=None, VigenciaInicial=None, VigenciaFinal=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.OptanteSimplesNacional = OptanteSimplesNacional
        self.OptanteSimplesNacional_nsprefix_ = None
        if isinstance(VigenciaInicial, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(VigenciaInicial, '%Y-%m-%d').date()
        else:
            initvalue_ = VigenciaInicial
        self.VigenciaInicial = initvalue_
        self.VigenciaInicial_nsprefix_ = None
        if isinstance(VigenciaFinal, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(VigenciaFinal, '%Y-%m-%d').date()
        else:
            initvalue_ = VigenciaFinal
        self.VigenciaFinal = initvalue_
        self.VigenciaFinal_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, tcSimplesNacional)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if tcSimplesNacional.subclass:
            return tcSimplesNacional.subclass(*args_, **kwargs_)
        else:
            return tcSimplesNacional(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_OptanteSimplesNacional(self):
        return self.OptanteSimplesNacional
    def set_OptanteSimplesNacional(self, OptanteSimplesNacional):
        self.OptanteSimplesNacional = OptanteSimplesNacional
    def get_VigenciaInicial(self):
        return self.VigenciaInicial
    def set_VigenciaInicial(self, VigenciaInicial):
        self.VigenciaInicial = VigenciaInicial
    def get_VigenciaFinal(self):
        return self.VigenciaFinal
    def set_VigenciaFinal(self, VigenciaFinal):
        self.VigenciaFinal = VigenciaFinal
    def hasContent_(self):
        if (
            self.OptanteSimplesNacional is not None or
            self.VigenciaInicial is not None or
            self.VigenciaFinal is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:ts="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_simples.xsd"  xmlns:None="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd" ', name_='tcSimplesNacional', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('tcSimplesNacional')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'tcSimplesNacional':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='tcSimplesNacional')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='tcSimplesNacional', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='tcSimplesNacional'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:ts="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_simples.xsd"  xmlns:None="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd" ', name_='tcSimplesNacional', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.OptanteSimplesNacional is not None:
            namespaceprefix_ = self.OptanteSimplesNacional_nsprefix_ + ':' if (UseCapturedNS_ and self.OptanteSimplesNacional_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sOptanteSimplesNacional>%s</%sOptanteSimplesNacional>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.OptanteSimplesNacional), input_name='OptanteSimplesNacional')), namespaceprefix_ , eol_))
        if self.VigenciaInicial is not None:
            namespaceprefix_ = self.VigenciaInicial_nsprefix_ + ':' if (UseCapturedNS_ and self.VigenciaInicial_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sVigenciaInicial>%s</%sVigenciaInicial>%s' % (namespaceprefix_ , self.gds_format_date(self.VigenciaInicial, input_name='VigenciaInicial'), namespaceprefix_ , eol_))
        if self.VigenciaFinal is not None:
            namespaceprefix_ = self.VigenciaFinal_nsprefix_ + ':' if (UseCapturedNS_ and self.VigenciaFinal_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sVigenciaFinal>%s</%sVigenciaFinal>%s' % (namespaceprefix_ , self.gds_format_date(self.VigenciaFinal, input_name='VigenciaFinal'), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'OptanteSimplesNacional':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'OptanteSimplesNacional')
            value_ = self.gds_validate_string(value_, node, 'OptanteSimplesNacional')
            self.OptanteSimplesNacional = value_
            self.OptanteSimplesNacional_nsprefix_ = child_.prefix
        elif nodeName_ == 'VigenciaInicial':
            sval_ = child_.text
            dval_ = self.gds_parse_date(sval_)
            self.VigenciaInicial = dval_
            self.VigenciaInicial_nsprefix_ = child_.prefix
        elif nodeName_ == 'VigenciaFinal':
            sval_ = child_.text
            dval_ = self.gds_parse_date(sval_)
            self.VigenciaFinal = dval_
            self.VigenciaFinal_nsprefix_ = child_.prefix
# end class tcSimplesNacional


class tcMei(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Mei=None, VigenciaInicial=None, VigenciaFinal=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Mei = Mei
        self.Mei_nsprefix_ = None
        if isinstance(VigenciaInicial, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(VigenciaInicial, '%Y-%m-%d').date()
        else:
            initvalue_ = VigenciaInicial
        self.VigenciaInicial = initvalue_
        self.VigenciaInicial_nsprefix_ = None
        if isinstance(VigenciaFinal, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(VigenciaFinal, '%Y-%m-%d').date()
        else:
            initvalue_ = VigenciaFinal
        self.VigenciaFinal = initvalue_
        self.VigenciaFinal_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, tcMei)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if tcMei.subclass:
            return tcMei.subclass(*args_, **kwargs_)
        else:
            return tcMei(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Mei(self):
        return self.Mei
    def set_Mei(self, Mei):
        self.Mei = Mei
    def get_VigenciaInicial(self):
        return self.VigenciaInicial
    def set_VigenciaInicial(self, VigenciaInicial):
        self.VigenciaInicial = VigenciaInicial
    def get_VigenciaFinal(self):
        return self.VigenciaFinal
    def set_VigenciaFinal(self, VigenciaFinal):
        self.VigenciaFinal = VigenciaFinal
    def hasContent_(self):
        if (
            self.Mei is not None or
            self.VigenciaInicial is not None or
            self.VigenciaFinal is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:ts="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_simples.xsd"  xmlns:None="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd" ', name_='tcMei', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('tcMei')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'tcMei':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='tcMei')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='tcMei', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='tcMei'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:ts="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_simples.xsd"  xmlns:None="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd" ', name_='tcMei', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Mei is not None:
            namespaceprefix_ = self.Mei_nsprefix_ + ':' if (UseCapturedNS_ and self.Mei_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sMei>%s</%sMei>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Mei), input_name='Mei')), namespaceprefix_ , eol_))
        if self.VigenciaInicial is not None:
            namespaceprefix_ = self.VigenciaInicial_nsprefix_ + ':' if (UseCapturedNS_ and self.VigenciaInicial_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sVigenciaInicial>%s</%sVigenciaInicial>%s' % (namespaceprefix_ , self.gds_format_date(self.VigenciaInicial, input_name='VigenciaInicial'), namespaceprefix_ , eol_))
        if self.VigenciaFinal is not None:
            namespaceprefix_ = self.VigenciaFinal_nsprefix_ + ':' if (UseCapturedNS_ and self.VigenciaFinal_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sVigenciaFinal>%s</%sVigenciaFinal>%s' % (namespaceprefix_ , self.gds_format_date(self.VigenciaFinal, input_name='VigenciaFinal'), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Mei':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Mei')
            value_ = self.gds_validate_string(value_, node, 'Mei')
            self.Mei = value_
            self.Mei_nsprefix_ = child_.prefix
        elif nodeName_ == 'VigenciaInicial':
            sval_ = child_.text
            dval_ = self.gds_parse_date(sval_)
            self.VigenciaInicial = dval_
            self.VigenciaInicial_nsprefix_ = child_.prefix
        elif nodeName_ == 'VigenciaFinal':
            sval_ = child_.text
            dval_ = self.gds_parse_date(sval_)
            self.VigenciaFinal = dval_
            self.VigenciaFinal_nsprefix_ = child_.prefix
# end class tcMei


class tcCnae(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, CodigoCnae=None, DescricaoCnae=None, Principal=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.CodigoCnae = CodigoCnae
        self.CodigoCnae_nsprefix_ = None
        self.DescricaoCnae = DescricaoCnae
        self.DescricaoCnae_nsprefix_ = None
        self.Principal = Principal
        self.Principal_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, tcCnae)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if tcCnae.subclass:
            return tcCnae.subclass(*args_, **kwargs_)
        else:
            return tcCnae(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_CodigoCnae(self):
        return self.CodigoCnae
    def set_CodigoCnae(self, CodigoCnae):
        self.CodigoCnae = CodigoCnae
    def get_DescricaoCnae(self):
        return self.DescricaoCnae
    def set_DescricaoCnae(self, DescricaoCnae):
        self.DescricaoCnae = DescricaoCnae
    def get_Principal(self):
        return self.Principal
    def set_Principal(self, Principal):
        self.Principal = Principal
    def hasContent_(self):
        if (
            self.CodigoCnae is not None or
            self.DescricaoCnae is not None or
            self.Principal is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd"  xmlns:ts="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_simples.xsd" ', name_='tcCnae', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('tcCnae')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'tcCnae':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='tcCnae')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='tcCnae', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='tcCnae'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd"  xmlns:ts="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_simples.xsd" ', name_='tcCnae', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.CodigoCnae is not None:
            namespaceprefix_ = self.CodigoCnae_nsprefix_ + ':' if (UseCapturedNS_ and self.CodigoCnae_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCodigoCnae>%s</%sCodigoCnae>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.CodigoCnae), input_name='CodigoCnae')), namespaceprefix_ , eol_))
        if self.DescricaoCnae is not None:
            namespaceprefix_ = self.DescricaoCnae_nsprefix_ + ':' if (UseCapturedNS_ and self.DescricaoCnae_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sDescricaoCnae>%s</%sDescricaoCnae>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.DescricaoCnae), input_name='DescricaoCnae')), namespaceprefix_ , eol_))
        if self.Principal is not None:
            namespaceprefix_ = self.Principal_nsprefix_ + ':' if (UseCapturedNS_ and self.Principal_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sPrincipal>%s</%sPrincipal>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Principal), input_name='Principal')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'CodigoCnae':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'CodigoCnae')
            value_ = self.gds_validate_string(value_, node, 'CodigoCnae')
            self.CodigoCnae = value_
            self.CodigoCnae_nsprefix_ = child_.prefix
        elif nodeName_ == 'DescricaoCnae':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'DescricaoCnae')
            value_ = self.gds_validate_string(value_, node, 'DescricaoCnae')
            self.DescricaoCnae = value_
            self.DescricaoCnae_nsprefix_ = child_.prefix
        elif nodeName_ == 'Principal':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Principal')
            value_ = self.gds_validate_string(value_, node, 'Principal')
            self.Principal = value_
            self.Principal_nsprefix_ = child_.prefix
# end class tcCnae


class tcNaturezaOperacao(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, CodigoNaturezaOperacao=None, DescricaoNaturezaOperacao=None, VigenciaInicial=None, VigenciaFinal=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.CodigoNaturezaOperacao = CodigoNaturezaOperacao
        self.CodigoNaturezaOperacao_nsprefix_ = None
        self.DescricaoNaturezaOperacao = DescricaoNaturezaOperacao
        self.DescricaoNaturezaOperacao_nsprefix_ = None
        if isinstance(VigenciaInicial, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(VigenciaInicial, '%Y-%m-%d').date()
        else:
            initvalue_ = VigenciaInicial
        self.VigenciaInicial = initvalue_
        self.VigenciaInicial_nsprefix_ = None
        if isinstance(VigenciaFinal, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(VigenciaFinal, '%Y-%m-%d').date()
        else:
            initvalue_ = VigenciaFinal
        self.VigenciaFinal = initvalue_
        self.VigenciaFinal_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, tcNaturezaOperacao)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if tcNaturezaOperacao.subclass:
            return tcNaturezaOperacao.subclass(*args_, **kwargs_)
        else:
            return tcNaturezaOperacao(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_CodigoNaturezaOperacao(self):
        return self.CodigoNaturezaOperacao
    def set_CodigoNaturezaOperacao(self, CodigoNaturezaOperacao):
        self.CodigoNaturezaOperacao = CodigoNaturezaOperacao
    def get_DescricaoNaturezaOperacao(self):
        return self.DescricaoNaturezaOperacao
    def set_DescricaoNaturezaOperacao(self, DescricaoNaturezaOperacao):
        self.DescricaoNaturezaOperacao = DescricaoNaturezaOperacao
    def get_VigenciaInicial(self):
        return self.VigenciaInicial
    def set_VigenciaInicial(self, VigenciaInicial):
        self.VigenciaInicial = VigenciaInicial
    def get_VigenciaFinal(self):
        return self.VigenciaFinal
    def set_VigenciaFinal(self, VigenciaFinal):
        self.VigenciaFinal = VigenciaFinal
    def hasContent_(self):
        if (
            self.CodigoNaturezaOperacao is not None or
            self.DescricaoNaturezaOperacao is not None or
            self.VigenciaInicial is not None or
            self.VigenciaFinal is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:ts="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_simples.xsd"  xmlns:None="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd" ', name_='tcNaturezaOperacao', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('tcNaturezaOperacao')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'tcNaturezaOperacao':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='tcNaturezaOperacao')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='tcNaturezaOperacao', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='tcNaturezaOperacao'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:ts="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_simples.xsd"  xmlns:None="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd" ', name_='tcNaturezaOperacao', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.CodigoNaturezaOperacao is not None:
            namespaceprefix_ = self.CodigoNaturezaOperacao_nsprefix_ + ':' if (UseCapturedNS_ and self.CodigoNaturezaOperacao_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCodigoNaturezaOperacao>%s</%sCodigoNaturezaOperacao>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.CodigoNaturezaOperacao), input_name='CodigoNaturezaOperacao')), namespaceprefix_ , eol_))
        if self.DescricaoNaturezaOperacao is not None:
            namespaceprefix_ = self.DescricaoNaturezaOperacao_nsprefix_ + ':' if (UseCapturedNS_ and self.DescricaoNaturezaOperacao_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sDescricaoNaturezaOperacao>%s</%sDescricaoNaturezaOperacao>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.DescricaoNaturezaOperacao), input_name='DescricaoNaturezaOperacao')), namespaceprefix_ , eol_))
        if self.VigenciaInicial is not None:
            namespaceprefix_ = self.VigenciaInicial_nsprefix_ + ':' if (UseCapturedNS_ and self.VigenciaInicial_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sVigenciaInicial>%s</%sVigenciaInicial>%s' % (namespaceprefix_ , self.gds_format_date(self.VigenciaInicial, input_name='VigenciaInicial'), namespaceprefix_ , eol_))
        if self.VigenciaFinal is not None:
            namespaceprefix_ = self.VigenciaFinal_nsprefix_ + ':' if (UseCapturedNS_ and self.VigenciaFinal_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sVigenciaFinal>%s</%sVigenciaFinal>%s' % (namespaceprefix_ , self.gds_format_date(self.VigenciaFinal, input_name='VigenciaFinal'), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'CodigoNaturezaOperacao':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'CodigoNaturezaOperacao')
            value_ = self.gds_validate_string(value_, node, 'CodigoNaturezaOperacao')
            self.CodigoNaturezaOperacao = value_
            self.CodigoNaturezaOperacao_nsprefix_ = child_.prefix
        elif nodeName_ == 'DescricaoNaturezaOperacao':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'DescricaoNaturezaOperacao')
            value_ = self.gds_validate_string(value_, node, 'DescricaoNaturezaOperacao')
            self.DescricaoNaturezaOperacao = value_
            self.DescricaoNaturezaOperacao_nsprefix_ = child_.prefix
        elif nodeName_ == 'VigenciaInicial':
            sval_ = child_.text
            dval_ = self.gds_parse_date(sval_)
            self.VigenciaInicial = dval_
            self.VigenciaInicial_nsprefix_ = child_.prefix
        elif nodeName_ == 'VigenciaFinal':
            sval_ = child_.text
            dval_ = self.gds_parse_date(sval_)
            self.VigenciaFinal = dval_
            self.VigenciaFinal_nsprefix_ = child_.prefix
# end class tcNaturezaOperacao


class tcIdentificacaoContribuinte(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, CpfCnpj=None, InscricaoMunicipal=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.CpfCnpj = CpfCnpj
        self.CpfCnpj_nsprefix_ = None
        self.InscricaoMunicipal = InscricaoMunicipal
        self.InscricaoMunicipal_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, tcIdentificacaoContribuinte)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if tcIdentificacaoContribuinte.subclass:
            return tcIdentificacaoContribuinte.subclass(*args_, **kwargs_)
        else:
            return tcIdentificacaoContribuinte(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_CpfCnpj(self):
        return self.CpfCnpj
    def set_CpfCnpj(self, CpfCnpj):
        self.CpfCnpj = CpfCnpj
    def get_InscricaoMunicipal(self):
        return self.InscricaoMunicipal
    def set_InscricaoMunicipal(self, InscricaoMunicipal):
        self.InscricaoMunicipal = InscricaoMunicipal
    def hasContent_(self):
        if (
            self.CpfCnpj is not None or
            self.InscricaoMunicipal is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd"  xmlns:ts="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_simples.xsd" ', name_='tcIdentificacaoContribuinte', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('tcIdentificacaoContribuinte')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'tcIdentificacaoContribuinte':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='tcIdentificacaoContribuinte')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='tcIdentificacaoContribuinte', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='tcIdentificacaoContribuinte'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd"  xmlns:ts="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_simples.xsd" ', name_='tcIdentificacaoContribuinte', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.CpfCnpj is not None:
            namespaceprefix_ = self.CpfCnpj_nsprefix_ + ':' if (UseCapturedNS_ and self.CpfCnpj_nsprefix_) else ''
            self.CpfCnpj.export(outfile, level, namespaceprefix_, namespacedef_='', name_='CpfCnpj', pretty_print=pretty_print)
        if self.InscricaoMunicipal is not None:
            namespaceprefix_ = self.InscricaoMunicipal_nsprefix_ + ':' if (UseCapturedNS_ and self.InscricaoMunicipal_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sInscricaoMunicipal>%s</%sInscricaoMunicipal>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.InscricaoMunicipal), input_name='InscricaoMunicipal')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'CpfCnpj':
            obj_ = tcCpfCnpj.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.CpfCnpj = obj_
            obj_.original_tagname_ = 'CpfCnpj'
        elif nodeName_ == 'InscricaoMunicipal':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'InscricaoMunicipal')
            value_ = self.gds_validate_string(value_, node, 'InscricaoMunicipal')
            self.InscricaoMunicipal = value_
            self.InscricaoMunicipal_nsprefix_ = child_.prefix
# end class tcIdentificacaoContribuinte


class tcInfRps(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, id=None, IdentificacaoRps=None, DataEmissao=None, NaturezaOperacao=None, RegimeEspecialTributacao=None, OptanteSimplesNacional=None, IncentivadorCultural=None, Status=None, RpsSubstituido=None, Servico=None, Prestador=None, Tomador=None, IntermediarioServico=None, ContrucaoCivil=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.id = _cast(None, id)
        self.id_nsprefix_ = None
        self.IdentificacaoRps = IdentificacaoRps
        self.IdentificacaoRps_nsprefix_ = None
        if isinstance(DataEmissao, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(DataEmissao, '%Y-%m-%dT%H:%M:%S')
        else:
            initvalue_ = DataEmissao
        self.DataEmissao = initvalue_
        self.DataEmissao_nsprefix_ = None
        self.NaturezaOperacao = NaturezaOperacao
        self.NaturezaOperacao_nsprefix_ = None
        self.RegimeEspecialTributacao = RegimeEspecialTributacao
        self.RegimeEspecialTributacao_nsprefix_ = None
        self.OptanteSimplesNacional = OptanteSimplesNacional
        self.OptanteSimplesNacional_nsprefix_ = None
        self.IncentivadorCultural = IncentivadorCultural
        self.IncentivadorCultural_nsprefix_ = None
        self.Status = Status
        self.Status_nsprefix_ = None
        self.RpsSubstituido = RpsSubstituido
        self.RpsSubstituido_nsprefix_ = None
        self.Servico = Servico
        self.Servico_nsprefix_ = None
        self.Prestador = Prestador
        self.Prestador_nsprefix_ = None
        self.Tomador = Tomador
        self.Tomador_nsprefix_ = None
        self.IntermediarioServico = IntermediarioServico
        self.IntermediarioServico_nsprefix_ = None
        self.ContrucaoCivil = ContrucaoCivil
        self.ContrucaoCivil_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, tcInfRps)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if tcInfRps.subclass:
            return tcInfRps.subclass(*args_, **kwargs_)
        else:
            return tcInfRps(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_IdentificacaoRps(self):
        return self.IdentificacaoRps
    def set_IdentificacaoRps(self, IdentificacaoRps):
        self.IdentificacaoRps = IdentificacaoRps
    def get_DataEmissao(self):
        return self.DataEmissao
    def set_DataEmissao(self, DataEmissao):
        self.DataEmissao = DataEmissao
    def get_NaturezaOperacao(self):
        return self.NaturezaOperacao
    def set_NaturezaOperacao(self, NaturezaOperacao):
        self.NaturezaOperacao = NaturezaOperacao
    def get_RegimeEspecialTributacao(self):
        return self.RegimeEspecialTributacao
    def set_RegimeEspecialTributacao(self, RegimeEspecialTributacao):
        self.RegimeEspecialTributacao = RegimeEspecialTributacao
    def get_OptanteSimplesNacional(self):
        return self.OptanteSimplesNacional
    def set_OptanteSimplesNacional(self, OptanteSimplesNacional):
        self.OptanteSimplesNacional = OptanteSimplesNacional
    def get_IncentivadorCultural(self):
        return self.IncentivadorCultural
    def set_IncentivadorCultural(self, IncentivadorCultural):
        self.IncentivadorCultural = IncentivadorCultural
    def get_Status(self):
        return self.Status
    def set_Status(self, Status):
        self.Status = Status
    def get_RpsSubstituido(self):
        return self.RpsSubstituido
    def set_RpsSubstituido(self, RpsSubstituido):
        self.RpsSubstituido = RpsSubstituido
    def get_Servico(self):
        return self.Servico
    def set_Servico(self, Servico):
        self.Servico = Servico
    def get_Prestador(self):
        return self.Prestador
    def set_Prestador(self, Prestador):
        self.Prestador = Prestador
    def get_Tomador(self):
        return self.Tomador
    def set_Tomador(self, Tomador):
        self.Tomador = Tomador
    def get_IntermediarioServico(self):
        return self.IntermediarioServico
    def set_IntermediarioServico(self, IntermediarioServico):
        self.IntermediarioServico = IntermediarioServico
    def get_ContrucaoCivil(self):
        return self.ContrucaoCivil
    def set_ContrucaoCivil(self, ContrucaoCivil):
        self.ContrucaoCivil = ContrucaoCivil
    def get_id(self):
        return self.id
    def set_id(self, id):
        self.id = id
    def hasContent_(self):
        if (
            self.IdentificacaoRps is not None or
            self.DataEmissao is not None or
            self.NaturezaOperacao is not None or
            self.RegimeEspecialTributacao is not None or
            self.OptanteSimplesNacional is not None or
            self.IncentivadorCultural is not None or
            self.Status is not None or
            self.RpsSubstituido is not None or
            self.Servico is not None or
            self.Prestador is not None or
            self.Tomador is not None or
            self.IntermediarioServico is not None or
            self.ContrucaoCivil is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd"  xmlns:ts="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_simples.xsd" ', name_='tcInfRps', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('tcInfRps')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'tcInfRps':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='tcInfRps')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='tcInfRps', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='tcInfRps'):
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (quote_attrib(self.id), ))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd"  xmlns:ts="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_simples.xsd" ', name_='tcInfRps', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.IdentificacaoRps is not None:
            namespaceprefix_ = self.IdentificacaoRps_nsprefix_ + ':' if (UseCapturedNS_ and self.IdentificacaoRps_nsprefix_) else ''
            self.IdentificacaoRps.export(outfile, level, namespaceprefix_, namespacedef_='', name_='IdentificacaoRps', pretty_print=pretty_print)
        if self.DataEmissao is not None:
            namespaceprefix_ = self.DataEmissao_nsprefix_ + ':' if (UseCapturedNS_ and self.DataEmissao_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sDataEmissao>%s</%sDataEmissao>%s' % (namespaceprefix_ , self.gds_format_datetime(self.DataEmissao, input_name='DataEmissao'), namespaceprefix_ , eol_))
        if self.NaturezaOperacao is not None:
            namespaceprefix_ = self.NaturezaOperacao_nsprefix_ + ':' if (UseCapturedNS_ and self.NaturezaOperacao_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sNaturezaOperacao>%s</%sNaturezaOperacao>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.NaturezaOperacao), input_name='NaturezaOperacao')), namespaceprefix_ , eol_))
        if self.RegimeEspecialTributacao is not None:
            namespaceprefix_ = self.RegimeEspecialTributacao_nsprefix_ + ':' if (UseCapturedNS_ and self.RegimeEspecialTributacao_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sRegimeEspecialTributacao>%s</%sRegimeEspecialTributacao>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.RegimeEspecialTributacao), input_name='RegimeEspecialTributacao')), namespaceprefix_ , eol_))
        if self.OptanteSimplesNacional is not None:
            namespaceprefix_ = self.OptanteSimplesNacional_nsprefix_ + ':' if (UseCapturedNS_ and self.OptanteSimplesNacional_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sOptanteSimplesNacional>%s</%sOptanteSimplesNacional>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.OptanteSimplesNacional), input_name='OptanteSimplesNacional')), namespaceprefix_ , eol_))
        if self.IncentivadorCultural is not None:
            namespaceprefix_ = self.IncentivadorCultural_nsprefix_ + ':' if (UseCapturedNS_ and self.IncentivadorCultural_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sIncentivadorCultural>%s</%sIncentivadorCultural>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.IncentivadorCultural), input_name='IncentivadorCultural')), namespaceprefix_ , eol_))
        if self.Status is not None:
            namespaceprefix_ = self.Status_nsprefix_ + ':' if (UseCapturedNS_ and self.Status_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sStatus>%s</%sStatus>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Status), input_name='Status')), namespaceprefix_ , eol_))
        if self.RpsSubstituido is not None:
            namespaceprefix_ = self.RpsSubstituido_nsprefix_ + ':' if (UseCapturedNS_ and self.RpsSubstituido_nsprefix_) else ''
            self.RpsSubstituido.export(outfile, level, namespaceprefix_, namespacedef_='', name_='RpsSubstituido', pretty_print=pretty_print)
        if self.Servico is not None:
            namespaceprefix_ = self.Servico_nsprefix_ + ':' if (UseCapturedNS_ and self.Servico_nsprefix_) else ''
            self.Servico.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Servico', pretty_print=pretty_print)
        if self.Prestador is not None:
            namespaceprefix_ = self.Prestador_nsprefix_ + ':' if (UseCapturedNS_ and self.Prestador_nsprefix_) else ''
            self.Prestador.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Prestador', pretty_print=pretty_print)
        if self.Tomador is not None:
            namespaceprefix_ = self.Tomador_nsprefix_ + ':' if (UseCapturedNS_ and self.Tomador_nsprefix_) else ''
            self.Tomador.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Tomador', pretty_print=pretty_print)
        if self.IntermediarioServico is not None:
            namespaceprefix_ = self.IntermediarioServico_nsprefix_ + ':' if (UseCapturedNS_ and self.IntermediarioServico_nsprefix_) else ''
            self.IntermediarioServico.export(outfile, level, namespaceprefix_, namespacedef_='', name_='IntermediarioServico', pretty_print=pretty_print)
        if self.ContrucaoCivil is not None:
            namespaceprefix_ = self.ContrucaoCivil_nsprefix_ + ':' if (UseCapturedNS_ and self.ContrucaoCivil_nsprefix_) else ''
            self.ContrucaoCivil.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ContrucaoCivil', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'IdentificacaoRps':
            obj_ = tcIdentificacaoRps.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.IdentificacaoRps = obj_
            obj_.original_tagname_ = 'IdentificacaoRps'
        elif nodeName_ == 'DataEmissao':
            sval_ = child_.text
            dval_ = self.gds_parse_datetime(sval_)
            self.DataEmissao = dval_
            self.DataEmissao_nsprefix_ = child_.prefix
        elif nodeName_ == 'NaturezaOperacao':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'NaturezaOperacao')
            value_ = self.gds_validate_string(value_, node, 'NaturezaOperacao')
            self.NaturezaOperacao = value_
            self.NaturezaOperacao_nsprefix_ = child_.prefix
        elif nodeName_ == 'RegimeEspecialTributacao':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'RegimeEspecialTributacao')
            value_ = self.gds_validate_string(value_, node, 'RegimeEspecialTributacao')
            self.RegimeEspecialTributacao = value_
            self.RegimeEspecialTributacao_nsprefix_ = child_.prefix
        elif nodeName_ == 'OptanteSimplesNacional':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'OptanteSimplesNacional')
            value_ = self.gds_validate_string(value_, node, 'OptanteSimplesNacional')
            self.OptanteSimplesNacional = value_
            self.OptanteSimplesNacional_nsprefix_ = child_.prefix
        elif nodeName_ == 'IncentivadorCultural':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'IncentivadorCultural')
            value_ = self.gds_validate_string(value_, node, 'IncentivadorCultural')
            self.IncentivadorCultural = value_
            self.IncentivadorCultural_nsprefix_ = child_.prefix
        elif nodeName_ == 'Status':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Status')
            value_ = self.gds_validate_string(value_, node, 'Status')
            self.Status = value_
            self.Status_nsprefix_ = child_.prefix
        elif nodeName_ == 'RpsSubstituido':
            obj_ = tcIdentificacaoRps.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.RpsSubstituido = obj_
            obj_.original_tagname_ = 'RpsSubstituido'
        elif nodeName_ == 'Servico':
            obj_ = tcDadosServico.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Servico = obj_
            obj_.original_tagname_ = 'Servico'
        elif nodeName_ == 'Prestador':
            obj_ = tcIdentificacaoPrestador.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Prestador = obj_
            obj_.original_tagname_ = 'Prestador'
        elif nodeName_ == 'Tomador':
            obj_ = tcDadosTomador.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Tomador = obj_
            obj_.original_tagname_ = 'Tomador'
        elif nodeName_ == 'IntermediarioServico':
            obj_ = tcIdentificacaoIntermediarioServico.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.IntermediarioServico = obj_
            obj_.original_tagname_ = 'IntermediarioServico'
        elif nodeName_ == 'ContrucaoCivil':
            obj_ = tcDadosConstrucaoCivil.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ContrucaoCivil = obj_
            obj_.original_tagname_ = 'ContrucaoCivil'
# end class tcInfRps


class tcRps(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, InfRps=None, Signature=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.InfRps = InfRps
        self.InfRps_nsprefix_ = None
        self.Signature = Signature
        self.Signature_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, tcRps)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if tcRps.subclass:
            return tcRps.subclass(*args_, **kwargs_)
        else:
            return tcRps(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_InfRps(self):
        return self.InfRps
    def set_InfRps(self, InfRps):
        self.InfRps = InfRps
    def get_Signature(self):
        return self.Signature
    def set_Signature(self, Signature):
        self.Signature = Signature
    def hasContent_(self):
        if (
            self.InfRps is not None or
            self.Signature is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd"  xmlns:dsig="http://www.w3.org/2000/09/xmldsig#" ', name_='tcRps', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('tcRps')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'tcRps':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='tcRps')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='tcRps', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='tcRps'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd"  xmlns:dsig="http://www.w3.org/2000/09/xmldsig#" ', name_='tcRps', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.InfRps is not None:
            namespaceprefix_ = self.InfRps_nsprefix_ + ':' if (UseCapturedNS_ and self.InfRps_nsprefix_) else ''
            self.InfRps.export(outfile, level, namespaceprefix_, namespacedef_='', name_='InfRps', pretty_print=pretty_print)
        if self.Signature is not None:
            namespaceprefix_ = self.Signature_nsprefix_ + ':' if (UseCapturedNS_ and self.Signature_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sSignature>%s</%sSignature>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Signature), input_name='Signature')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'InfRps':
            obj_ = tcInfRps.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.InfRps = obj_
            obj_.original_tagname_ = 'InfRps'
        elif nodeName_ == 'Signature':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Signature')
            value_ = self.gds_validate_string(value_, node, 'Signature')
            self.Signature = value_
            self.Signature_nsprefix_ = child_.prefix
# end class tcRps


class tcIdentificacaoNfse(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Numero=None, Cnpj=None, InscricaoMunicipal=None, CodigoMunicipio=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Numero = Numero
        self.Numero_nsprefix_ = None
        self.Cnpj = Cnpj
        self.Cnpj_nsprefix_ = None
        self.InscricaoMunicipal = InscricaoMunicipal
        self.InscricaoMunicipal_nsprefix_ = None
        self.CodigoMunicipio = CodigoMunicipio
        self.CodigoMunicipio_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, tcIdentificacaoNfse)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if tcIdentificacaoNfse.subclass:
            return tcIdentificacaoNfse.subclass(*args_, **kwargs_)
        else:
            return tcIdentificacaoNfse(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Numero(self):
        return self.Numero
    def set_Numero(self, Numero):
        self.Numero = Numero
    def get_Cnpj(self):
        return self.Cnpj
    def set_Cnpj(self, Cnpj):
        self.Cnpj = Cnpj
    def get_InscricaoMunicipal(self):
        return self.InscricaoMunicipal
    def set_InscricaoMunicipal(self, InscricaoMunicipal):
        self.InscricaoMunicipal = InscricaoMunicipal
    def get_CodigoMunicipio(self):
        return self.CodigoMunicipio
    def set_CodigoMunicipio(self, CodigoMunicipio):
        self.CodigoMunicipio = CodigoMunicipio
    def hasContent_(self):
        if (
            self.Numero is not None or
            self.Cnpj is not None or
            self.InscricaoMunicipal is not None or
            self.CodigoMunicipio is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:ts="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_simples.xsd" ', name_='tcIdentificacaoNfse', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('tcIdentificacaoNfse')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'tcIdentificacaoNfse':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='tcIdentificacaoNfse')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='tcIdentificacaoNfse', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='tcIdentificacaoNfse'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:ts="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_simples.xsd" ', name_='tcIdentificacaoNfse', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Numero is not None:
            namespaceprefix_ = self.Numero_nsprefix_ + ':' if (UseCapturedNS_ and self.Numero_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sNumero>%s</%sNumero>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Numero), input_name='Numero')), namespaceprefix_ , eol_))
        if self.Cnpj is not None:
            namespaceprefix_ = self.Cnpj_nsprefix_ + ':' if (UseCapturedNS_ and self.Cnpj_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCnpj>%s</%sCnpj>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Cnpj), input_name='Cnpj')), namespaceprefix_ , eol_))
        if self.InscricaoMunicipal is not None:
            namespaceprefix_ = self.InscricaoMunicipal_nsprefix_ + ':' if (UseCapturedNS_ and self.InscricaoMunicipal_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sInscricaoMunicipal>%s</%sInscricaoMunicipal>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.InscricaoMunicipal), input_name='InscricaoMunicipal')), namespaceprefix_ , eol_))
        if self.CodigoMunicipio is not None:
            namespaceprefix_ = self.CodigoMunicipio_nsprefix_ + ':' if (UseCapturedNS_ and self.CodigoMunicipio_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCodigoMunicipio>%s</%sCodigoMunicipio>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.CodigoMunicipio), input_name='CodigoMunicipio')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Numero':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Numero')
            value_ = self.gds_validate_string(value_, node, 'Numero')
            self.Numero = value_
            self.Numero_nsprefix_ = child_.prefix
        elif nodeName_ == 'Cnpj':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Cnpj')
            value_ = self.gds_validate_string(value_, node, 'Cnpj')
            self.Cnpj = value_
            self.Cnpj_nsprefix_ = child_.prefix
        elif nodeName_ == 'InscricaoMunicipal':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'InscricaoMunicipal')
            value_ = self.gds_validate_string(value_, node, 'InscricaoMunicipal')
            self.InscricaoMunicipal = value_
            self.InscricaoMunicipal_nsprefix_ = child_.prefix
        elif nodeName_ == 'CodigoMunicipio':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'CodigoMunicipio')
            value_ = self.gds_validate_string(value_, node, 'CodigoMunicipio')
            self.CodigoMunicipio = value_
            self.CodigoMunicipio_nsprefix_ = child_.prefix
# end class tcIdentificacaoNfse


class tcInfNfse(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, id=None, Numero=None, CodigoVerificacao=None, DataEmissao=None, IdentificacaoRps=None, DataEmissaoRps=None, NaturezaOperacao=None, RegimeEspecialTributacao=None, OptanteSimplesNacional=None, IncentivadorCultural=None, Competencia=None, NfseSubstituida=None, OutrasInformacoes=None, Servico=None, ValorCredito=None, PrestadorServico=None, TomadorServico=None, IntermediarioServico=None, OrgaoGerador=None, ContrucaoCivil=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.id = _cast(None, id)
        self.id_nsprefix_ = None
        self.Numero = Numero
        self.Numero_nsprefix_ = None
        self.CodigoVerificacao = CodigoVerificacao
        self.CodigoVerificacao_nsprefix_ = None
        if isinstance(DataEmissao, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(DataEmissao, '%Y-%m-%dT%H:%M:%S')
        else:
            initvalue_ = DataEmissao
        self.DataEmissao = initvalue_
        self.DataEmissao_nsprefix_ = None
        self.IdentificacaoRps = IdentificacaoRps
        self.IdentificacaoRps_nsprefix_ = None
        if isinstance(DataEmissaoRps, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(DataEmissaoRps, '%Y-%m-%dT%H:%M:%S')
        else:
            initvalue_ = DataEmissaoRps
        self.DataEmissaoRps = initvalue_
        self.DataEmissaoRps_nsprefix_ = None
        self.NaturezaOperacao = NaturezaOperacao
        self.NaturezaOperacao_nsprefix_ = None
        self.RegimeEspecialTributacao = RegimeEspecialTributacao
        self.RegimeEspecialTributacao_nsprefix_ = None
        self.OptanteSimplesNacional = OptanteSimplesNacional
        self.OptanteSimplesNacional_nsprefix_ = None
        self.IncentivadorCultural = IncentivadorCultural
        self.IncentivadorCultural_nsprefix_ = None
        self.Competencia = Competencia
        self.Competencia_nsprefix_ = None
        self.NfseSubstituida = NfseSubstituida
        self.NfseSubstituida_nsprefix_ = None
        self.OutrasInformacoes = OutrasInformacoes
        self.OutrasInformacoes_nsprefix_ = None
        self.Servico = Servico
        self.Servico_nsprefix_ = None
        self.ValorCredito = ValorCredito
        self.ValorCredito_nsprefix_ = None
        self.PrestadorServico = PrestadorServico
        self.PrestadorServico_nsprefix_ = None
        self.TomadorServico = TomadorServico
        self.TomadorServico_nsprefix_ = None
        self.IntermediarioServico = IntermediarioServico
        self.IntermediarioServico_nsprefix_ = None
        self.OrgaoGerador = OrgaoGerador
        self.OrgaoGerador_nsprefix_ = None
        self.ContrucaoCivil = ContrucaoCivil
        self.ContrucaoCivil_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, tcInfNfse)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if tcInfNfse.subclass:
            return tcInfNfse.subclass(*args_, **kwargs_)
        else:
            return tcInfNfse(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Numero(self):
        return self.Numero
    def set_Numero(self, Numero):
        self.Numero = Numero
    def get_CodigoVerificacao(self):
        return self.CodigoVerificacao
    def set_CodigoVerificacao(self, CodigoVerificacao):
        self.CodigoVerificacao = CodigoVerificacao
    def get_DataEmissao(self):
        return self.DataEmissao
    def set_DataEmissao(self, DataEmissao):
        self.DataEmissao = DataEmissao
    def get_IdentificacaoRps(self):
        return self.IdentificacaoRps
    def set_IdentificacaoRps(self, IdentificacaoRps):
        self.IdentificacaoRps = IdentificacaoRps
    def get_DataEmissaoRps(self):
        return self.DataEmissaoRps
    def set_DataEmissaoRps(self, DataEmissaoRps):
        self.DataEmissaoRps = DataEmissaoRps
    def get_NaturezaOperacao(self):
        return self.NaturezaOperacao
    def set_NaturezaOperacao(self, NaturezaOperacao):
        self.NaturezaOperacao = NaturezaOperacao
    def get_RegimeEspecialTributacao(self):
        return self.RegimeEspecialTributacao
    def set_RegimeEspecialTributacao(self, RegimeEspecialTributacao):
        self.RegimeEspecialTributacao = RegimeEspecialTributacao
    def get_OptanteSimplesNacional(self):
        return self.OptanteSimplesNacional
    def set_OptanteSimplesNacional(self, OptanteSimplesNacional):
        self.OptanteSimplesNacional = OptanteSimplesNacional
    def get_IncentivadorCultural(self):
        return self.IncentivadorCultural
    def set_IncentivadorCultural(self, IncentivadorCultural):
        self.IncentivadorCultural = IncentivadorCultural
    def get_Competencia(self):
        return self.Competencia
    def set_Competencia(self, Competencia):
        self.Competencia = Competencia
    def get_NfseSubstituida(self):
        return self.NfseSubstituida
    def set_NfseSubstituida(self, NfseSubstituida):
        self.NfseSubstituida = NfseSubstituida
    def get_OutrasInformacoes(self):
        return self.OutrasInformacoes
    def set_OutrasInformacoes(self, OutrasInformacoes):
        self.OutrasInformacoes = OutrasInformacoes
    def get_Servico(self):
        return self.Servico
    def set_Servico(self, Servico):
        self.Servico = Servico
    def get_ValorCredito(self):
        return self.ValorCredito
    def set_ValorCredito(self, ValorCredito):
        self.ValorCredito = ValorCredito
    def get_PrestadorServico(self):
        return self.PrestadorServico
    def set_PrestadorServico(self, PrestadorServico):
        self.PrestadorServico = PrestadorServico
    def get_TomadorServico(self):
        return self.TomadorServico
    def set_TomadorServico(self, TomadorServico):
        self.TomadorServico = TomadorServico
    def get_IntermediarioServico(self):
        return self.IntermediarioServico
    def set_IntermediarioServico(self, IntermediarioServico):
        self.IntermediarioServico = IntermediarioServico
    def get_OrgaoGerador(self):
        return self.OrgaoGerador
    def set_OrgaoGerador(self, OrgaoGerador):
        self.OrgaoGerador = OrgaoGerador
    def get_ContrucaoCivil(self):
        return self.ContrucaoCivil
    def set_ContrucaoCivil(self, ContrucaoCivil):
        self.ContrucaoCivil = ContrucaoCivil
    def get_id(self):
        return self.id
    def set_id(self, id):
        self.id = id
    def hasContent_(self):
        if (
            self.Numero is not None or
            self.CodigoVerificacao is not None or
            self.DataEmissao is not None or
            self.IdentificacaoRps is not None or
            self.DataEmissaoRps is not None or
            self.NaturezaOperacao is not None or
            self.RegimeEspecialTributacao is not None or
            self.OptanteSimplesNacional is not None or
            self.IncentivadorCultural is not None or
            self.Competencia is not None or
            self.NfseSubstituida is not None or
            self.OutrasInformacoes is not None or
            self.Servico is not None or
            self.ValorCredito is not None or
            self.PrestadorServico is not None or
            self.TomadorServico is not None or
            self.IntermediarioServico is not None or
            self.OrgaoGerador is not None or
            self.ContrucaoCivil is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:ts="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_simples.xsd"  xmlns:None="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd" ', name_='tcInfNfse', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('tcInfNfse')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'tcInfNfse':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='tcInfNfse')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='tcInfNfse', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='tcInfNfse'):
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (quote_attrib(self.id), ))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:ts="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_simples.xsd"  xmlns:None="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd" ', name_='tcInfNfse', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Numero is not None:
            namespaceprefix_ = self.Numero_nsprefix_ + ':' if (UseCapturedNS_ and self.Numero_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sNumero>%s</%sNumero>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Numero), input_name='Numero')), namespaceprefix_ , eol_))
        if self.CodigoVerificacao is not None:
            namespaceprefix_ = self.CodigoVerificacao_nsprefix_ + ':' if (UseCapturedNS_ and self.CodigoVerificacao_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCodigoVerificacao>%s</%sCodigoVerificacao>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.CodigoVerificacao), input_name='CodigoVerificacao')), namespaceprefix_ , eol_))
        if self.DataEmissao is not None:
            namespaceprefix_ = self.DataEmissao_nsprefix_ + ':' if (UseCapturedNS_ and self.DataEmissao_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sDataEmissao>%s</%sDataEmissao>%s' % (namespaceprefix_ , self.gds_format_datetime(self.DataEmissao, input_name='DataEmissao'), namespaceprefix_ , eol_))
        if self.IdentificacaoRps is not None:
            namespaceprefix_ = self.IdentificacaoRps_nsprefix_ + ':' if (UseCapturedNS_ and self.IdentificacaoRps_nsprefix_) else ''
            self.IdentificacaoRps.export(outfile, level, namespaceprefix_, namespacedef_='', name_='IdentificacaoRps', pretty_print=pretty_print)
        if self.DataEmissaoRps is not None:
            namespaceprefix_ = self.DataEmissaoRps_nsprefix_ + ':' if (UseCapturedNS_ and self.DataEmissaoRps_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sDataEmissaoRps>%s</%sDataEmissaoRps>%s' % (namespaceprefix_ , self.gds_format_datetime(self.DataEmissaoRps, input_name='DataEmissaoRps'), namespaceprefix_ , eol_))
        if self.NaturezaOperacao is not None:
            namespaceprefix_ = self.NaturezaOperacao_nsprefix_ + ':' if (UseCapturedNS_ and self.NaturezaOperacao_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sNaturezaOperacao>%s</%sNaturezaOperacao>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.NaturezaOperacao), input_name='NaturezaOperacao')), namespaceprefix_ , eol_))
        if self.RegimeEspecialTributacao is not None:
            namespaceprefix_ = self.RegimeEspecialTributacao_nsprefix_ + ':' if (UseCapturedNS_ and self.RegimeEspecialTributacao_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sRegimeEspecialTributacao>%s</%sRegimeEspecialTributacao>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.RegimeEspecialTributacao), input_name='RegimeEspecialTributacao')), namespaceprefix_ , eol_))
        if self.OptanteSimplesNacional is not None:
            namespaceprefix_ = self.OptanteSimplesNacional_nsprefix_ + ':' if (UseCapturedNS_ and self.OptanteSimplesNacional_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sOptanteSimplesNacional>%s</%sOptanteSimplesNacional>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.OptanteSimplesNacional), input_name='OptanteSimplesNacional')), namespaceprefix_ , eol_))
        if self.IncentivadorCultural is not None:
            namespaceprefix_ = self.IncentivadorCultural_nsprefix_ + ':' if (UseCapturedNS_ and self.IncentivadorCultural_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sIncentivadorCultural>%s</%sIncentivadorCultural>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.IncentivadorCultural), input_name='IncentivadorCultural')), namespaceprefix_ , eol_))
        if self.Competencia is not None:
            namespaceprefix_ = self.Competencia_nsprefix_ + ':' if (UseCapturedNS_ and self.Competencia_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCompetencia>%s</%sCompetencia>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Competencia), input_name='Competencia')), namespaceprefix_ , eol_))
        if self.NfseSubstituida is not None:
            namespaceprefix_ = self.NfseSubstituida_nsprefix_ + ':' if (UseCapturedNS_ and self.NfseSubstituida_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sNfseSubstituida>%s</%sNfseSubstituida>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.NfseSubstituida), input_name='NfseSubstituida')), namespaceprefix_ , eol_))
        if self.OutrasInformacoes is not None:
            namespaceprefix_ = self.OutrasInformacoes_nsprefix_ + ':' if (UseCapturedNS_ and self.OutrasInformacoes_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sOutrasInformacoes>%s</%sOutrasInformacoes>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.OutrasInformacoes), input_name='OutrasInformacoes')), namespaceprefix_ , eol_))
        if self.Servico is not None:
            namespaceprefix_ = self.Servico_nsprefix_ + ':' if (UseCapturedNS_ and self.Servico_nsprefix_) else ''
            self.Servico.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Servico', pretty_print=pretty_print)
        if self.ValorCredito is not None:
            namespaceprefix_ = self.ValorCredito_nsprefix_ + ':' if (UseCapturedNS_ and self.ValorCredito_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sValorCredito>%s</%sValorCredito>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.ValorCredito), input_name='ValorCredito')), namespaceprefix_ , eol_))
        if self.PrestadorServico is not None:
            namespaceprefix_ = self.PrestadorServico_nsprefix_ + ':' if (UseCapturedNS_ and self.PrestadorServico_nsprefix_) else ''
            self.PrestadorServico.export(outfile, level, namespaceprefix_, namespacedef_='', name_='PrestadorServico', pretty_print=pretty_print)
        if self.TomadorServico is not None:
            namespaceprefix_ = self.TomadorServico_nsprefix_ + ':' if (UseCapturedNS_ and self.TomadorServico_nsprefix_) else ''
            self.TomadorServico.export(outfile, level, namespaceprefix_, namespacedef_='', name_='TomadorServico', pretty_print=pretty_print)
        if self.IntermediarioServico is not None:
            namespaceprefix_ = self.IntermediarioServico_nsprefix_ + ':' if (UseCapturedNS_ and self.IntermediarioServico_nsprefix_) else ''
            self.IntermediarioServico.export(outfile, level, namespaceprefix_, namespacedef_='', name_='IntermediarioServico', pretty_print=pretty_print)
        if self.OrgaoGerador is not None:
            namespaceprefix_ = self.OrgaoGerador_nsprefix_ + ':' if (UseCapturedNS_ and self.OrgaoGerador_nsprefix_) else ''
            self.OrgaoGerador.export(outfile, level, namespaceprefix_, namespacedef_='', name_='OrgaoGerador', pretty_print=pretty_print)
        if self.ContrucaoCivil is not None:
            namespaceprefix_ = self.ContrucaoCivil_nsprefix_ + ':' if (UseCapturedNS_ and self.ContrucaoCivil_nsprefix_) else ''
            self.ContrucaoCivil.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ContrucaoCivil', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Numero':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Numero')
            value_ = self.gds_validate_string(value_, node, 'Numero')
            self.Numero = value_
            self.Numero_nsprefix_ = child_.prefix
        elif nodeName_ == 'CodigoVerificacao':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'CodigoVerificacao')
            value_ = self.gds_validate_string(value_, node, 'CodigoVerificacao')
            self.CodigoVerificacao = value_
            self.CodigoVerificacao_nsprefix_ = child_.prefix
        elif nodeName_ == 'DataEmissao':
            sval_ = child_.text
            dval_ = self.gds_parse_datetime(sval_)
            self.DataEmissao = dval_
            self.DataEmissao_nsprefix_ = child_.prefix
        elif nodeName_ == 'IdentificacaoRps':
            obj_ = tcIdentificacaoRps.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.IdentificacaoRps = obj_
            obj_.original_tagname_ = 'IdentificacaoRps'
        elif nodeName_ == 'DataEmissaoRps':
            sval_ = child_.text
            dval_ = self.gds_parse_datetime(sval_)
            self.DataEmissaoRps = dval_
            self.DataEmissaoRps_nsprefix_ = child_.prefix
        elif nodeName_ == 'NaturezaOperacao':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'NaturezaOperacao')
            value_ = self.gds_validate_string(value_, node, 'NaturezaOperacao')
            self.NaturezaOperacao = value_
            self.NaturezaOperacao_nsprefix_ = child_.prefix
        elif nodeName_ == 'RegimeEspecialTributacao':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'RegimeEspecialTributacao')
            value_ = self.gds_validate_string(value_, node, 'RegimeEspecialTributacao')
            self.RegimeEspecialTributacao = value_
            self.RegimeEspecialTributacao_nsprefix_ = child_.prefix
        elif nodeName_ == 'OptanteSimplesNacional':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'OptanteSimplesNacional')
            value_ = self.gds_validate_string(value_, node, 'OptanteSimplesNacional')
            self.OptanteSimplesNacional = value_
            self.OptanteSimplesNacional_nsprefix_ = child_.prefix
        elif nodeName_ == 'IncentivadorCultural':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'IncentivadorCultural')
            value_ = self.gds_validate_string(value_, node, 'IncentivadorCultural')
            self.IncentivadorCultural = value_
            self.IncentivadorCultural_nsprefix_ = child_.prefix
        elif nodeName_ == 'Competencia':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Competencia')
            value_ = self.gds_validate_string(value_, node, 'Competencia')
            self.Competencia = value_
            self.Competencia_nsprefix_ = child_.prefix
        elif nodeName_ == 'NfseSubstituida':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'NfseSubstituida')
            value_ = self.gds_validate_string(value_, node, 'NfseSubstituida')
            self.NfseSubstituida = value_
            self.NfseSubstituida_nsprefix_ = child_.prefix
        elif nodeName_ == 'OutrasInformacoes':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'OutrasInformacoes')
            value_ = self.gds_validate_string(value_, node, 'OutrasInformacoes')
            self.OutrasInformacoes = value_
            self.OutrasInformacoes_nsprefix_ = child_.prefix
        elif nodeName_ == 'Servico':
            obj_ = tcDadosServico.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Servico = obj_
            obj_.original_tagname_ = 'Servico'
        elif nodeName_ == 'ValorCredito':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'ValorCredito')
            value_ = self.gds_validate_string(value_, node, 'ValorCredito')
            self.ValorCredito = value_
            self.ValorCredito_nsprefix_ = child_.prefix
        elif nodeName_ == 'PrestadorServico':
            obj_ = tcDadosPrestador.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.PrestadorServico = obj_
            obj_.original_tagname_ = 'PrestadorServico'
        elif nodeName_ == 'TomadorServico':
            obj_ = tcDadosTomador.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.TomadorServico = obj_
            obj_.original_tagname_ = 'TomadorServico'
        elif nodeName_ == 'IntermediarioServico':
            obj_ = tcIdentificacaoIntermediarioServico.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.IntermediarioServico = obj_
            obj_.original_tagname_ = 'IntermediarioServico'
        elif nodeName_ == 'OrgaoGerador':
            obj_ = tcIdentificacaoOrgaoGerador.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.OrgaoGerador = obj_
            obj_.original_tagname_ = 'OrgaoGerador'
        elif nodeName_ == 'ContrucaoCivil':
            obj_ = tcDadosConstrucaoCivil.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ContrucaoCivil = obj_
            obj_.original_tagname_ = 'ContrucaoCivil'
# end class tcInfNfse


class tcNfse(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, InfNfse=None, Signature=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.InfNfse = InfNfse
        self.InfNfse_nsprefix_ = None
        if Signature is None:
            self.Signature = []
        else:
            self.Signature = Signature
        self.Signature_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, tcNfse)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if tcNfse.subclass:
            return tcNfse.subclass(*args_, **kwargs_)
        else:
            return tcNfse(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_InfNfse(self):
        return self.InfNfse
    def set_InfNfse(self, InfNfse):
        self.InfNfse = InfNfse
    def get_Signature(self):
        return self.Signature
    def set_Signature(self, Signature):
        self.Signature = Signature
    def add_Signature(self, value):
        self.Signature.append(value)
    def insert_Signature_at(self, index, value):
        self.Signature.insert(index, value)
    def replace_Signature_at(self, index, value):
        self.Signature[index] = value
    def hasContent_(self):
        if (
            self.InfNfse is not None or
            self.Signature
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd"  xmlns:dsig="http://www.w3.org/2000/09/xmldsig#" ', name_='tcNfse', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('tcNfse')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'tcNfse':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='tcNfse')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='tcNfse', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='tcNfse'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd"  xmlns:dsig="http://www.w3.org/2000/09/xmldsig#" ', name_='tcNfse', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.InfNfse is not None:
            namespaceprefix_ = self.InfNfse_nsprefix_ + ':' if (UseCapturedNS_ and self.InfNfse_nsprefix_) else ''
            self.InfNfse.export(outfile, level, namespaceprefix_, namespacedef_='', name_='InfNfse', pretty_print=pretty_print)
        for Signature_ in self.Signature:
            namespaceprefix_ = self.Signature_nsprefix_ + ':' if (UseCapturedNS_ and self.Signature_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sSignature>%s</%sSignature>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(Signature_), input_name='Signature')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'InfNfse':
            obj_ = tcInfNfse.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.InfNfse = obj_
            obj_.original_tagname_ = 'InfNfse'
        elif nodeName_ == 'Signature':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Signature')
            value_ = self.gds_validate_string(value_, node, 'Signature')
            self.Signature.append(value_)
            self.Signature_nsprefix_ = child_.prefix
# end class tcNfse


class tcInfPedidoCancelamento(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, id=None, IdentificacaoNfse=None, CodigoCancelamento=None, MotivoCancelamentoNfse=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.id = _cast(None, id)
        self.id_nsprefix_ = None
        self.IdentificacaoNfse = IdentificacaoNfse
        self.IdentificacaoNfse_nsprefix_ = None
        self.CodigoCancelamento = CodigoCancelamento
        self.CodigoCancelamento_nsprefix_ = None
        self.MotivoCancelamentoNfse = MotivoCancelamentoNfse
        self.MotivoCancelamentoNfse_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, tcInfPedidoCancelamento)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if tcInfPedidoCancelamento.subclass:
            return tcInfPedidoCancelamento.subclass(*args_, **kwargs_)
        else:
            return tcInfPedidoCancelamento(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_IdentificacaoNfse(self):
        return self.IdentificacaoNfse
    def set_IdentificacaoNfse(self, IdentificacaoNfse):
        self.IdentificacaoNfse = IdentificacaoNfse
    def get_CodigoCancelamento(self):
        return self.CodigoCancelamento
    def set_CodigoCancelamento(self, CodigoCancelamento):
        self.CodigoCancelamento = CodigoCancelamento
    def get_MotivoCancelamentoNfse(self):
        return self.MotivoCancelamentoNfse
    def set_MotivoCancelamentoNfse(self, MotivoCancelamentoNfse):
        self.MotivoCancelamentoNfse = MotivoCancelamentoNfse
    def get_id(self):
        return self.id
    def set_id(self, id):
        self.id = id
    def hasContent_(self):
        if (
            self.IdentificacaoNfse is not None or
            self.CodigoCancelamento is not None or
            self.MotivoCancelamentoNfse is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd"  xmlns:ts="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_simples.xsd" ', name_='tcInfPedidoCancelamento', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('tcInfPedidoCancelamento')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'tcInfPedidoCancelamento':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='tcInfPedidoCancelamento')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='tcInfPedidoCancelamento', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='tcInfPedidoCancelamento'):
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (quote_attrib(self.id), ))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd"  xmlns:ts="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_simples.xsd" ', name_='tcInfPedidoCancelamento', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.IdentificacaoNfse is not None:
            namespaceprefix_ = self.IdentificacaoNfse_nsprefix_ + ':' if (UseCapturedNS_ and self.IdentificacaoNfse_nsprefix_) else ''
            self.IdentificacaoNfse.export(outfile, level, namespaceprefix_, namespacedef_='', name_='IdentificacaoNfse', pretty_print=pretty_print)
        if self.CodigoCancelamento is not None:
            namespaceprefix_ = self.CodigoCancelamento_nsprefix_ + ':' if (UseCapturedNS_ and self.CodigoCancelamento_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCodigoCancelamento>%s</%sCodigoCancelamento>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.CodigoCancelamento), input_name='CodigoCancelamento')), namespaceprefix_ , eol_))
        if self.MotivoCancelamentoNfse is not None:
            namespaceprefix_ = self.MotivoCancelamentoNfse_nsprefix_ + ':' if (UseCapturedNS_ and self.MotivoCancelamentoNfse_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sMotivoCancelamentoNfse>%s</%sMotivoCancelamentoNfse>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.MotivoCancelamentoNfse), input_name='MotivoCancelamentoNfse')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'IdentificacaoNfse':
            obj_ = tcIdentificacaoNfse.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.IdentificacaoNfse = obj_
            obj_.original_tagname_ = 'IdentificacaoNfse'
        elif nodeName_ == 'CodigoCancelamento':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'CodigoCancelamento')
            value_ = self.gds_validate_string(value_, node, 'CodigoCancelamento')
            self.CodigoCancelamento = value_
            self.CodigoCancelamento_nsprefix_ = child_.prefix
        elif nodeName_ == 'MotivoCancelamentoNfse':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'MotivoCancelamentoNfse')
            value_ = self.gds_validate_string(value_, node, 'MotivoCancelamentoNfse')
            self.MotivoCancelamentoNfse = value_
            self.MotivoCancelamentoNfse_nsprefix_ = child_.prefix
# end class tcInfPedidoCancelamento


class tcPedidoCancelamento(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, InfPedidoCancelamento=None, Signature=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.InfPedidoCancelamento = InfPedidoCancelamento
        self.InfPedidoCancelamento_nsprefix_ = None
        self.Signature = Signature
        self.Signature_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, tcPedidoCancelamento)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if tcPedidoCancelamento.subclass:
            return tcPedidoCancelamento.subclass(*args_, **kwargs_)
        else:
            return tcPedidoCancelamento(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_InfPedidoCancelamento(self):
        return self.InfPedidoCancelamento
    def set_InfPedidoCancelamento(self, InfPedidoCancelamento):
        self.InfPedidoCancelamento = InfPedidoCancelamento
    def get_Signature(self):
        return self.Signature
    def set_Signature(self, Signature):
        self.Signature = Signature
    def hasContent_(self):
        if (
            self.InfPedidoCancelamento is not None or
            self.Signature is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd"  xmlns:dsig="http://www.w3.org/2000/09/xmldsig#" ', name_='tcPedidoCancelamento', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('tcPedidoCancelamento')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'tcPedidoCancelamento':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='tcPedidoCancelamento')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='tcPedidoCancelamento', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='tcPedidoCancelamento'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd"  xmlns:dsig="http://www.w3.org/2000/09/xmldsig#" ', name_='tcPedidoCancelamento', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.InfPedidoCancelamento is not None:
            namespaceprefix_ = self.InfPedidoCancelamento_nsprefix_ + ':' if (UseCapturedNS_ and self.InfPedidoCancelamento_nsprefix_) else ''
            self.InfPedidoCancelamento.export(outfile, level, namespaceprefix_, namespacedef_='', name_='InfPedidoCancelamento', pretty_print=pretty_print)
        if self.Signature is not None:
            namespaceprefix_ = self.Signature_nsprefix_ + ':' if (UseCapturedNS_ and self.Signature_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sSignature>%s</%sSignature>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Signature), input_name='Signature')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'InfPedidoCancelamento':
            obj_ = tcInfPedidoCancelamento.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.InfPedidoCancelamento = obj_
            obj_.original_tagname_ = 'InfPedidoCancelamento'
        elif nodeName_ == 'Signature':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Signature')
            value_ = self.gds_validate_string(value_, node, 'Signature')
            self.Signature = value_
            self.Signature_nsprefix_ = child_.prefix
# end class tcPedidoCancelamento


class tcInfConfirmacaoCancelamento(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Sucesso=None, DataHora=None, ListaMensagemRetorno=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Sucesso = Sucesso
        self.Sucesso_nsprefix_ = None
        if isinstance(DataHora, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(DataHora, '%Y-%m-%dT%H:%M:%S')
        else:
            initvalue_ = DataHora
        self.DataHora = initvalue_
        self.DataHora_nsprefix_ = None
        self.ListaMensagemRetorno = ListaMensagemRetorno
        self.ListaMensagemRetorno_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, tcInfConfirmacaoCancelamento)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if tcInfConfirmacaoCancelamento.subclass:
            return tcInfConfirmacaoCancelamento.subclass(*args_, **kwargs_)
        else:
            return tcInfConfirmacaoCancelamento(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Sucesso(self):
        return self.Sucesso
    def set_Sucesso(self, Sucesso):
        self.Sucesso = Sucesso
    def get_DataHora(self):
        return self.DataHora
    def set_DataHora(self, DataHora):
        self.DataHora = DataHora
    def get_ListaMensagemRetorno(self):
        return self.ListaMensagemRetorno
    def set_ListaMensagemRetorno(self, ListaMensagemRetorno):
        self.ListaMensagemRetorno = ListaMensagemRetorno
    def hasContent_(self):
        if (
            self.Sucesso is not None or
            self.DataHora is not None or
            self.ListaMensagemRetorno is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd" ', name_='tcInfConfirmacaoCancelamento', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('tcInfConfirmacaoCancelamento')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'tcInfConfirmacaoCancelamento':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='tcInfConfirmacaoCancelamento')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='tcInfConfirmacaoCancelamento', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='tcInfConfirmacaoCancelamento'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd" ', name_='tcInfConfirmacaoCancelamento', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Sucesso is not None:
            namespaceprefix_ = self.Sucesso_nsprefix_ + ':' if (UseCapturedNS_ and self.Sucesso_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sSucesso>%s</%sSucesso>%s' % (namespaceprefix_ , self.gds_format_boolean(self.Sucesso, input_name='Sucesso'), namespaceprefix_ , eol_))
        if self.DataHora is not None:
            namespaceprefix_ = self.DataHora_nsprefix_ + ':' if (UseCapturedNS_ and self.DataHora_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sDataHora>%s</%sDataHora>%s' % (namespaceprefix_ , self.gds_format_datetime(self.DataHora, input_name='DataHora'), namespaceprefix_ , eol_))
        if self.ListaMensagemRetorno is not None:
            namespaceprefix_ = self.ListaMensagemRetorno_nsprefix_ + ':' if (UseCapturedNS_ and self.ListaMensagemRetorno_nsprefix_) else ''
            self.ListaMensagemRetorno.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ListaMensagemRetorno', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Sucesso':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'Sucesso')
            ival_ = self.gds_validate_boolean(ival_, node, 'Sucesso')
            self.Sucesso = ival_
            self.Sucesso_nsprefix_ = child_.prefix
        elif nodeName_ == 'DataHora':
            sval_ = child_.text
            dval_ = self.gds_parse_datetime(sval_)
            self.DataHora = dval_
            self.DataHora_nsprefix_ = child_.prefix
        elif nodeName_ == 'ListaMensagemRetorno':
            obj_ = ListaMensagemRetornoType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ListaMensagemRetorno = obj_
            obj_.original_tagname_ = 'ListaMensagemRetorno'
# end class tcInfConfirmacaoCancelamento


class tcConfirmacaoCancelamento(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, id=None, Pedido=None, InfConfirmacaoCancelamento=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.id = _cast(None, id)
        self.id_nsprefix_ = None
        self.Pedido = Pedido
        self.Pedido_nsprefix_ = None
        self.InfConfirmacaoCancelamento = InfConfirmacaoCancelamento
        self.InfConfirmacaoCancelamento_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, tcConfirmacaoCancelamento)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if tcConfirmacaoCancelamento.subclass:
            return tcConfirmacaoCancelamento.subclass(*args_, **kwargs_)
        else:
            return tcConfirmacaoCancelamento(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Pedido(self):
        return self.Pedido
    def set_Pedido(self, Pedido):
        self.Pedido = Pedido
    def get_InfConfirmacaoCancelamento(self):
        return self.InfConfirmacaoCancelamento
    def set_InfConfirmacaoCancelamento(self, InfConfirmacaoCancelamento):
        self.InfConfirmacaoCancelamento = InfConfirmacaoCancelamento
    def get_id(self):
        return self.id
    def set_id(self, id):
        self.id = id
    def hasContent_(self):
        if (
            self.Pedido is not None or
            self.InfConfirmacaoCancelamento is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd" ', name_='tcConfirmacaoCancelamento', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('tcConfirmacaoCancelamento')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'tcConfirmacaoCancelamento':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='tcConfirmacaoCancelamento')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='tcConfirmacaoCancelamento', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='tcConfirmacaoCancelamento'):
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (quote_attrib(self.id), ))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd" ', name_='tcConfirmacaoCancelamento', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Pedido is not None:
            namespaceprefix_ = self.Pedido_nsprefix_ + ':' if (UseCapturedNS_ and self.Pedido_nsprefix_) else ''
            self.Pedido.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Pedido', pretty_print=pretty_print)
        if self.InfConfirmacaoCancelamento is not None:
            namespaceprefix_ = self.InfConfirmacaoCancelamento_nsprefix_ + ':' if (UseCapturedNS_ and self.InfConfirmacaoCancelamento_nsprefix_) else ''
            self.InfConfirmacaoCancelamento.export(outfile, level, namespaceprefix_, namespacedef_='', name_='InfConfirmacaoCancelamento', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Pedido':
            obj_ = tcPedidoCancelamento.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Pedido = obj_
            obj_.original_tagname_ = 'Pedido'
        elif nodeName_ == 'InfConfirmacaoCancelamento':
            obj_ = tcInfConfirmacaoCancelamento.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.InfConfirmacaoCancelamento = obj_
            obj_.original_tagname_ = 'InfConfirmacaoCancelamento'
# end class tcConfirmacaoCancelamento


class tcCancelamentoNfse(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Confirmacao=None, Signature=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Confirmacao = Confirmacao
        self.Confirmacao_nsprefix_ = None
        self.Signature = Signature
        self.Signature_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, tcCancelamentoNfse)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if tcCancelamentoNfse.subclass:
            return tcCancelamentoNfse.subclass(*args_, **kwargs_)
        else:
            return tcCancelamentoNfse(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Confirmacao(self):
        return self.Confirmacao
    def set_Confirmacao(self, Confirmacao):
        self.Confirmacao = Confirmacao
    def get_Signature(self):
        return self.Signature
    def set_Signature(self, Signature):
        self.Signature = Signature
    def hasContent_(self):
        if (
            self.Confirmacao is not None or
            self.Signature is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd"  xmlns:dsig="http://www.w3.org/2000/09/xmldsig#" ', name_='tcCancelamentoNfse', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('tcCancelamentoNfse')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'tcCancelamentoNfse':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='tcCancelamentoNfse')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='tcCancelamentoNfse', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='tcCancelamentoNfse'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd"  xmlns:dsig="http://www.w3.org/2000/09/xmldsig#" ', name_='tcCancelamentoNfse', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Confirmacao is not None:
            namespaceprefix_ = self.Confirmacao_nsprefix_ + ':' if (UseCapturedNS_ and self.Confirmacao_nsprefix_) else ''
            self.Confirmacao.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Confirmacao', pretty_print=pretty_print)
        if self.Signature is not None:
            namespaceprefix_ = self.Signature_nsprefix_ + ':' if (UseCapturedNS_ and self.Signature_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sSignature>%s</%sSignature>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Signature), input_name='Signature')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Confirmacao':
            obj_ = tcConfirmacaoCancelamento.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Confirmacao = obj_
            obj_.original_tagname_ = 'Confirmacao'
        elif nodeName_ == 'Signature':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Signature')
            value_ = self.gds_validate_string(value_, node, 'Signature')
            self.Signature = value_
            self.Signature_nsprefix_ = child_.prefix
# end class tcCancelamentoNfse


class tcInfSubstituicaoNfse(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, id=None, NfseSubstituidora=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.id = _cast(None, id)
        self.id_nsprefix_ = None
        self.NfseSubstituidora = NfseSubstituidora
        self.NfseSubstituidora_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, tcInfSubstituicaoNfse)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if tcInfSubstituicaoNfse.subclass:
            return tcInfSubstituicaoNfse.subclass(*args_, **kwargs_)
        else:
            return tcInfSubstituicaoNfse(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_NfseSubstituidora(self):
        return self.NfseSubstituidora
    def set_NfseSubstituidora(self, NfseSubstituidora):
        self.NfseSubstituidora = NfseSubstituidora
    def get_id(self):
        return self.id
    def set_id(self, id):
        self.id = id
    def hasContent_(self):
        if (
            self.NfseSubstituidora is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:ts="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_simples.xsd" ', name_='tcInfSubstituicaoNfse', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('tcInfSubstituicaoNfse')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'tcInfSubstituicaoNfse':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='tcInfSubstituicaoNfse')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='tcInfSubstituicaoNfse', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='tcInfSubstituicaoNfse'):
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (quote_attrib(self.id), ))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:ts="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_simples.xsd" ', name_='tcInfSubstituicaoNfse', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.NfseSubstituidora is not None:
            namespaceprefix_ = self.NfseSubstituidora_nsprefix_ + ':' if (UseCapturedNS_ and self.NfseSubstituidora_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sNfseSubstituidora>%s</%sNfseSubstituidora>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.NfseSubstituidora), input_name='NfseSubstituidora')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'NfseSubstituidora':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'NfseSubstituidora')
            value_ = self.gds_validate_string(value_, node, 'NfseSubstituidora')
            self.NfseSubstituidora = value_
            self.NfseSubstituidora_nsprefix_ = child_.prefix
# end class tcInfSubstituicaoNfse


class tcSubstituicaoNfse(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, SubstituicaoNfse=None, Signature=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.SubstituicaoNfse = SubstituicaoNfse
        self.SubstituicaoNfse_nsprefix_ = None
        if Signature is None:
            self.Signature = []
        else:
            self.Signature = Signature
        self.Signature_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, tcSubstituicaoNfse)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if tcSubstituicaoNfse.subclass:
            return tcSubstituicaoNfse.subclass(*args_, **kwargs_)
        else:
            return tcSubstituicaoNfse(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_SubstituicaoNfse(self):
        return self.SubstituicaoNfse
    def set_SubstituicaoNfse(self, SubstituicaoNfse):
        self.SubstituicaoNfse = SubstituicaoNfse
    def get_Signature(self):
        return self.Signature
    def set_Signature(self, Signature):
        self.Signature = Signature
    def add_Signature(self, value):
        self.Signature.append(value)
    def insert_Signature_at(self, index, value):
        self.Signature.insert(index, value)
    def replace_Signature_at(self, index, value):
        self.Signature[index] = value
    def hasContent_(self):
        if (
            self.SubstituicaoNfse is not None or
            self.Signature
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd"  xmlns:dsig="http://www.w3.org/2000/09/xmldsig#" ', name_='tcSubstituicaoNfse', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('tcSubstituicaoNfse')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'tcSubstituicaoNfse':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='tcSubstituicaoNfse')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='tcSubstituicaoNfse', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='tcSubstituicaoNfse'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd"  xmlns:dsig="http://www.w3.org/2000/09/xmldsig#" ', name_='tcSubstituicaoNfse', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.SubstituicaoNfse is not None:
            namespaceprefix_ = self.SubstituicaoNfse_nsprefix_ + ':' if (UseCapturedNS_ and self.SubstituicaoNfse_nsprefix_) else ''
            self.SubstituicaoNfse.export(outfile, level, namespaceprefix_, namespacedef_='', name_='SubstituicaoNfse', pretty_print=pretty_print)
        for Signature_ in self.Signature:
            namespaceprefix_ = self.Signature_nsprefix_ + ':' if (UseCapturedNS_ and self.Signature_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sSignature>%s</%sSignature>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(Signature_), input_name='Signature')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'SubstituicaoNfse':
            obj_ = tcInfSubstituicaoNfse.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.SubstituicaoNfse = obj_
            obj_.original_tagname_ = 'SubstituicaoNfse'
        elif nodeName_ == 'Signature':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Signature')
            value_ = self.gds_validate_string(value_, node, 'Signature')
            self.Signature.append(value_)
            self.Signature_nsprefix_ = child_.prefix
# end class tcSubstituicaoNfse


class tcCompNfse(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Nfse=None, NfseCancelamento=None, NfseSubstituicao=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Nfse = Nfse
        self.Nfse_nsprefix_ = None
        self.NfseCancelamento = NfseCancelamento
        self.NfseCancelamento_nsprefix_ = None
        self.NfseSubstituicao = NfseSubstituicao
        self.NfseSubstituicao_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, tcCompNfse)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if tcCompNfse.subclass:
            return tcCompNfse.subclass(*args_, **kwargs_)
        else:
            return tcCompNfse(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Nfse(self):
        return self.Nfse
    def set_Nfse(self, Nfse):
        self.Nfse = Nfse
    def get_NfseCancelamento(self):
        return self.NfseCancelamento
    def set_NfseCancelamento(self, NfseCancelamento):
        self.NfseCancelamento = NfseCancelamento
    def get_NfseSubstituicao(self):
        return self.NfseSubstituicao
    def set_NfseSubstituicao(self, NfseSubstituicao):
        self.NfseSubstituicao = NfseSubstituicao
    def hasContent_(self):
        if (
            self.Nfse is not None or
            self.NfseCancelamento is not None or
            self.NfseSubstituicao is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd" ', name_='tcCompNfse', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('tcCompNfse')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'tcCompNfse':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='tcCompNfse')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='tcCompNfse', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='tcCompNfse'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd" ', name_='tcCompNfse', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Nfse is not None:
            namespaceprefix_ = self.Nfse_nsprefix_ + ':' if (UseCapturedNS_ and self.Nfse_nsprefix_) else ''
            self.Nfse.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Nfse', pretty_print=pretty_print)
        if self.NfseCancelamento is not None:
            namespaceprefix_ = self.NfseCancelamento_nsprefix_ + ':' if (UseCapturedNS_ and self.NfseCancelamento_nsprefix_) else ''
            self.NfseCancelamento.export(outfile, level, namespaceprefix_, namespacedef_='', name_='NfseCancelamento', pretty_print=pretty_print)
        if self.NfseSubstituicao is not None:
            namespaceprefix_ = self.NfseSubstituicao_nsprefix_ + ':' if (UseCapturedNS_ and self.NfseSubstituicao_nsprefix_) else ''
            self.NfseSubstituicao.export(outfile, level, namespaceprefix_, namespacedef_='', name_='NfseSubstituicao', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Nfse':
            obj_ = tcNfse.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Nfse = obj_
            obj_.original_tagname_ = 'Nfse'
        elif nodeName_ == 'NfseCancelamento':
            obj_ = tcCancelamentoNfse.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.NfseCancelamento = obj_
            obj_.original_tagname_ = 'NfseCancelamento'
        elif nodeName_ == 'NfseSubstituicao':
            obj_ = tcSubstituicaoNfse.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.NfseSubstituicao = obj_
            obj_.original_tagname_ = 'NfseSubstituicao'
# end class tcCompNfse


class tcMensagemRetorno(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Codigo=None, Mensagem=None, Correcao=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Codigo = Codigo
        self.Codigo_nsprefix_ = None
        self.Mensagem = Mensagem
        self.Mensagem_nsprefix_ = None
        self.Correcao = Correcao
        self.Correcao_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, tcMensagemRetorno)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if tcMensagemRetorno.subclass:
            return tcMensagemRetorno.subclass(*args_, **kwargs_)
        else:
            return tcMensagemRetorno(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Codigo(self):
        return self.Codigo
    def set_Codigo(self, Codigo):
        self.Codigo = Codigo
    def get_Mensagem(self):
        return self.Mensagem
    def set_Mensagem(self, Mensagem):
        self.Mensagem = Mensagem
    def get_Correcao(self):
        return self.Correcao
    def set_Correcao(self, Correcao):
        self.Correcao = Correcao
    def hasContent_(self):
        if (
            self.Codigo is not None or
            self.Mensagem is not None or
            self.Correcao is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:ts="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_simples.xsd" ', name_='tcMensagemRetorno', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('tcMensagemRetorno')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'tcMensagemRetorno':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='tcMensagemRetorno')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='tcMensagemRetorno', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='tcMensagemRetorno'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:ts="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_simples.xsd" ', name_='tcMensagemRetorno', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Codigo is not None:
            namespaceprefix_ = self.Codigo_nsprefix_ + ':' if (UseCapturedNS_ and self.Codigo_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCodigo>%s</%sCodigo>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Codigo), input_name='Codigo')), namespaceprefix_ , eol_))
        if self.Mensagem is not None:
            namespaceprefix_ = self.Mensagem_nsprefix_ + ':' if (UseCapturedNS_ and self.Mensagem_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sMensagem>%s</%sMensagem>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Mensagem), input_name='Mensagem')), namespaceprefix_ , eol_))
        if self.Correcao is not None:
            namespaceprefix_ = self.Correcao_nsprefix_ + ':' if (UseCapturedNS_ and self.Correcao_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCorrecao>%s</%sCorrecao>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Correcao), input_name='Correcao')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Codigo':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Codigo')
            value_ = self.gds_validate_string(value_, node, 'Codigo')
            self.Codigo = value_
            self.Codigo_nsprefix_ = child_.prefix
        elif nodeName_ == 'Mensagem':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Mensagem')
            value_ = self.gds_validate_string(value_, node, 'Mensagem')
            self.Mensagem = value_
            self.Mensagem_nsprefix_ = child_.prefix
        elif nodeName_ == 'Correcao':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Correcao')
            value_ = self.gds_validate_string(value_, node, 'Correcao')
            self.Correcao = value_
            self.Correcao_nsprefix_ = child_.prefix
# end class tcMensagemRetorno


class tcMensagemRetornoLote(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, IdentificacaoRps=None, Codigo=None, Mensagem=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.IdentificacaoRps = IdentificacaoRps
        self.IdentificacaoRps_nsprefix_ = None
        self.Codigo = Codigo
        self.Codigo_nsprefix_ = None
        self.Mensagem = Mensagem
        self.Mensagem_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, tcMensagemRetornoLote)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if tcMensagemRetornoLote.subclass:
            return tcMensagemRetornoLote.subclass(*args_, **kwargs_)
        else:
            return tcMensagemRetornoLote(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_IdentificacaoRps(self):
        return self.IdentificacaoRps
    def set_IdentificacaoRps(self, IdentificacaoRps):
        self.IdentificacaoRps = IdentificacaoRps
    def get_Codigo(self):
        return self.Codigo
    def set_Codigo(self, Codigo):
        self.Codigo = Codigo
    def get_Mensagem(self):
        return self.Mensagem
    def set_Mensagem(self, Mensagem):
        self.Mensagem = Mensagem
    def hasContent_(self):
        if (
            self.IdentificacaoRps is not None or
            self.Codigo is not None or
            self.Mensagem is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd"  xmlns:ts="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_simples.xsd" ', name_='tcMensagemRetornoLote', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('tcMensagemRetornoLote')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'tcMensagemRetornoLote':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='tcMensagemRetornoLote')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='tcMensagemRetornoLote', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='tcMensagemRetornoLote'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd"  xmlns:ts="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_simples.xsd" ', name_='tcMensagemRetornoLote', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.IdentificacaoRps is not None:
            namespaceprefix_ = self.IdentificacaoRps_nsprefix_ + ':' if (UseCapturedNS_ and self.IdentificacaoRps_nsprefix_) else ''
            self.IdentificacaoRps.export(outfile, level, namespaceprefix_, namespacedef_='', name_='IdentificacaoRps', pretty_print=pretty_print)
        if self.Codigo is not None:
            namespaceprefix_ = self.Codigo_nsprefix_ + ':' if (UseCapturedNS_ and self.Codigo_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCodigo>%s</%sCodigo>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Codigo), input_name='Codigo')), namespaceprefix_ , eol_))
        if self.Mensagem is not None:
            namespaceprefix_ = self.Mensagem_nsprefix_ + ':' if (UseCapturedNS_ and self.Mensagem_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sMensagem>%s</%sMensagem>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Mensagem), input_name='Mensagem')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'IdentificacaoRps':
            obj_ = tcIdentificacaoRps.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.IdentificacaoRps = obj_
            obj_.original_tagname_ = 'IdentificacaoRps'
        elif nodeName_ == 'Codigo':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Codigo')
            value_ = self.gds_validate_string(value_, node, 'Codigo')
            self.Codigo = value_
            self.Codigo_nsprefix_ = child_.prefix
        elif nodeName_ == 'Mensagem':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Mensagem')
            value_ = self.gds_validate_string(value_, node, 'Mensagem')
            self.Mensagem = value_
            self.Mensagem_nsprefix_ = child_.prefix
# end class tcMensagemRetornoLote


class tcLoteRps(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, id=None, NumeroLote=None, CpfCnpj=None, InscricaoMunicipal=None, QuantidadeRps=None, ListaRps=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.id = _cast(None, id)
        self.id_nsprefix_ = None
        self.NumeroLote = NumeroLote
        self.NumeroLote_nsprefix_ = None
        self.CpfCnpj = CpfCnpj
        self.CpfCnpj_nsprefix_ = None
        self.InscricaoMunicipal = InscricaoMunicipal
        self.InscricaoMunicipal_nsprefix_ = None
        self.QuantidadeRps = QuantidadeRps
        self.QuantidadeRps_nsprefix_ = None
        self.ListaRps = ListaRps
        self.ListaRps_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, tcLoteRps)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if tcLoteRps.subclass:
            return tcLoteRps.subclass(*args_, **kwargs_)
        else:
            return tcLoteRps(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_NumeroLote(self):
        return self.NumeroLote
    def set_NumeroLote(self, NumeroLote):
        self.NumeroLote = NumeroLote
    def get_CpfCnpj(self):
        return self.CpfCnpj
    def set_CpfCnpj(self, CpfCnpj):
        self.CpfCnpj = CpfCnpj
    def get_InscricaoMunicipal(self):
        return self.InscricaoMunicipal
    def set_InscricaoMunicipal(self, InscricaoMunicipal):
        self.InscricaoMunicipal = InscricaoMunicipal
    def get_QuantidadeRps(self):
        return self.QuantidadeRps
    def set_QuantidadeRps(self, QuantidadeRps):
        self.QuantidadeRps = QuantidadeRps
    def get_ListaRps(self):
        return self.ListaRps
    def set_ListaRps(self, ListaRps):
        self.ListaRps = ListaRps
    def get_id(self):
        return self.id
    def set_id(self, id):
        self.id = id
    def hasContent_(self):
        if (
            self.NumeroLote is not None or
            self.CpfCnpj is not None or
            self.InscricaoMunicipal is not None or
            self.QuantidadeRps is not None or
            self.ListaRps is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:ts="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_simples.xsd"  xmlns:None="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd" ', name_='tcLoteRps', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('tcLoteRps')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'tcLoteRps':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='tcLoteRps')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='tcLoteRps', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='tcLoteRps'):
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (quote_attrib(self.id), ))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:ts="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_simples.xsd"  xmlns:None="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd" ', name_='tcLoteRps', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.NumeroLote is not None:
            namespaceprefix_ = self.NumeroLote_nsprefix_ + ':' if (UseCapturedNS_ and self.NumeroLote_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sNumeroLote>%s</%sNumeroLote>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.NumeroLote), input_name='NumeroLote')), namespaceprefix_ , eol_))
        if self.CpfCnpj is not None:
            namespaceprefix_ = self.CpfCnpj_nsprefix_ + ':' if (UseCapturedNS_ and self.CpfCnpj_nsprefix_) else ''
            self.CpfCnpj.export(outfile, level, namespaceprefix_, namespacedef_='', name_='CpfCnpj', pretty_print=pretty_print)
        if self.InscricaoMunicipal is not None:
            namespaceprefix_ = self.InscricaoMunicipal_nsprefix_ + ':' if (UseCapturedNS_ and self.InscricaoMunicipal_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sInscricaoMunicipal>%s</%sInscricaoMunicipal>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.InscricaoMunicipal), input_name='InscricaoMunicipal')), namespaceprefix_ , eol_))
        if self.QuantidadeRps is not None:
            namespaceprefix_ = self.QuantidadeRps_nsprefix_ + ':' if (UseCapturedNS_ and self.QuantidadeRps_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sQuantidadeRps>%s</%sQuantidadeRps>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.QuantidadeRps), input_name='QuantidadeRps')), namespaceprefix_ , eol_))
        if self.ListaRps is not None:
            namespaceprefix_ = self.ListaRps_nsprefix_ + ':' if (UseCapturedNS_ and self.ListaRps_nsprefix_) else ''
            self.ListaRps.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ListaRps', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'NumeroLote':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'NumeroLote')
            value_ = self.gds_validate_string(value_, node, 'NumeroLote')
            self.NumeroLote = value_
            self.NumeroLote_nsprefix_ = child_.prefix
        elif nodeName_ == 'CpfCnpj':
            obj_ = tcCpfCnpj.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.CpfCnpj = obj_
            obj_.original_tagname_ = 'CpfCnpj'
        elif nodeName_ == 'InscricaoMunicipal':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'InscricaoMunicipal')
            value_ = self.gds_validate_string(value_, node, 'InscricaoMunicipal')
            self.InscricaoMunicipal = value_
            self.InscricaoMunicipal_nsprefix_ = child_.prefix
        elif nodeName_ == 'QuantidadeRps':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'QuantidadeRps')
            value_ = self.gds_validate_string(value_, node, 'QuantidadeRps')
            self.QuantidadeRps = value_
            self.QuantidadeRps_nsprefix_ = child_.prefix
        elif nodeName_ == 'ListaRps':
            obj_ = ListaRpsType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ListaRps = obj_
            obj_.original_tagname_ = 'ListaRps'
# end class tcLoteRps


class ListaMensagemRetornoType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, MensagemRetorno=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if MensagemRetorno is None:
            self.MensagemRetorno = []
        else:
            self.MensagemRetorno = MensagemRetorno
        self.MensagemRetorno_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ListaMensagemRetornoType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ListaMensagemRetornoType.subclass:
            return ListaMensagemRetornoType.subclass(*args_, **kwargs_)
        else:
            return ListaMensagemRetornoType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_MensagemRetorno(self):
        return self.MensagemRetorno
    def set_MensagemRetorno(self, MensagemRetorno):
        self.MensagemRetorno = MensagemRetorno
    def add_MensagemRetorno(self, value):
        self.MensagemRetorno.append(value)
    def insert_MensagemRetorno_at(self, index, value):
        self.MensagemRetorno.insert(index, value)
    def replace_MensagemRetorno_at(self, index, value):
        self.MensagemRetorno[index] = value
    def hasContent_(self):
        if (
            self.MensagemRetorno
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd" ', name_='ListaMensagemRetornoType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ListaMensagemRetornoType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ListaMensagemRetornoType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ListaMensagemRetornoType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ListaMensagemRetornoType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ListaMensagemRetornoType'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd" ', name_='ListaMensagemRetornoType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for MensagemRetorno_ in self.MensagemRetorno:
            namespaceprefix_ = self.MensagemRetorno_nsprefix_ + ':' if (UseCapturedNS_ and self.MensagemRetorno_nsprefix_) else ''
            MensagemRetorno_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='MensagemRetorno', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'MensagemRetorno':
            obj_ = tcMensagemRetorno.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.MensagemRetorno.append(obj_)
            obj_.original_tagname_ = 'MensagemRetorno'
# end class ListaMensagemRetornoType


class ListaRpsType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Rps=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if Rps is None:
            self.Rps = []
        else:
            self.Rps = Rps
        self.Rps_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ListaRpsType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ListaRpsType.subclass:
            return ListaRpsType.subclass(*args_, **kwargs_)
        else:
            return ListaRpsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Rps(self):
        return self.Rps
    def set_Rps(self, Rps):
        self.Rps = Rps
    def add_Rps(self, value):
        self.Rps.append(value)
    def insert_Rps_at(self, index, value):
        self.Rps.insert(index, value)
    def replace_Rps_at(self, index, value):
        self.Rps[index] = value
    def hasContent_(self):
        if (
            self.Rps
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd" ', name_='ListaRpsType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ListaRpsType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ListaRpsType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ListaRpsType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ListaRpsType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ListaRpsType'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd" ', name_='ListaRpsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Rps_ in self.Rps:
            namespaceprefix_ = self.Rps_nsprefix_ + ':' if (UseCapturedNS_ and self.Rps_nsprefix_) else ''
            Rps_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Rps', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Rps':
            obj_ = tcRps.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Rps.append(obj_)
            obj_.original_tagname_ = 'Rps'
# end class ListaRpsType


GDSClassesMapping = {
}


USAGE_TEXT = """
Usage: python <Parser>.py [ -s ] <in_xml_file>
"""


def usage():
    print(USAGE_TEXT)
    sys.exit(1)


def get_root_tag(node):
    tag = Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = GDSClassesMapping.get(tag)
    if rootClass is None:
        rootClass = globals().get(tag)
    return tag, rootClass


def get_required_ns_prefix_defs(rootNode):
    '''Get all name space prefix definitions required in this XML doc.
    Return a dictionary of definitions and a char string of definitions.
    '''
    nsmap = {
        prefix: uri
        for node in rootNode.iter()
        for (prefix, uri) in node.nsmap.items()
        if prefix is not None
    }
    namespacedefs = ' '.join([
        'xmlns:{}="{}"'.format(prefix, uri)
        for prefix, uri in nsmap.items()
    ])
    return nsmap, namespacedefs


def parse(inFileName, silence=False, print_warnings=True):
    global CapturedNsmap_
    gds_collector = GdsCollector_()
    parser = None
    doc = parsexml_(inFileName, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'tcCpfCnpj'
        rootClass = tcCpfCnpj
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    CapturedNsmap_, namespacedefs = get_required_ns_prefix_defs(rootNode)
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_=namespacedefs,
            pretty_print=True)
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ('-' * 50) + '\n'
        sys.stderr.write(separator)
        sys.stderr.write('----- Warnings -- count: {} -----\n'.format(
            len(gds_collector.get_messages()), ))
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj


def parseEtree(inFileName, silence=False, print_warnings=True,
               mapping=None, nsmap=None):
    parser = None
    doc = parsexml_(inFileName, parser)
    gds_collector = GdsCollector_()
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'tcCpfCnpj'
        rootClass = tcCpfCnpj
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    # Enable Python to collect the space used by the DOM.
    if mapping is None:
        mapping = {}
    rootElement = rootObj.to_etree(
        None, name_=rootTag, mapping_=mapping, nsmap_=nsmap)
    reverse_mapping = rootObj.gds_reverse_node_mapping(mapping)
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        content = etree_.tostring(
            rootElement, pretty_print=True,
            xml_declaration=True, encoding="utf-8")
        sys.stdout.write(str(content))
        sys.stdout.write('\n')
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ('-' * 50) + '\n'
        sys.stderr.write(separator)
        sys.stderr.write('----- Warnings -- count: {} -----\n'.format(
            len(gds_collector.get_messages()), ))
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj, rootElement, mapping, reverse_mapping


def parseString(inString, silence=False, print_warnings=True):
    '''Parse a string, create the object tree, and export it.

    Arguments:
    - inString -- A string.  This XML fragment should not start
      with an XML declaration containing an encoding.
    - silence -- A boolean.  If False, export the object.
    Returns -- The root object in the tree.
    '''
    parser = None
    rootNode= parsexmlstring_(inString, parser)
    gds_collector = GdsCollector_()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'tcCpfCnpj'
        rootClass = tcCpfCnpj
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    if not SaveElementTreeNode:
        rootNode = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='')
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ('-' * 50) + '\n'
        sys.stderr.write(separator)
        sys.stderr.write('----- Warnings -- count: {} -----\n'.format(
            len(gds_collector.get_messages()), ))
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj


def parseLiteral(inFileName, silence=False, print_warnings=True):
    parser = None
    doc = parsexml_(inFileName, parser)
    gds_collector = GdsCollector_()
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'tcCpfCnpj'
        rootClass = tcCpfCnpj
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        sys.stdout.write('#from Servico_Cancelar_justificativa_tipo_complexos import *\n\n')
        sys.stdout.write('import Servico_Cancelar_justificativa_tipo_complexos as model_\n\n')
        sys.stdout.write('rootObj = model_.rootClass(\n')
        rootObj.exportLiteral(sys.stdout, 0, name_=rootTag)
        sys.stdout.write(')\n')
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ('-' * 50) + '\n'
        sys.stderr.write(separator)
        sys.stderr.write('----- Warnings -- count: {} -----\n'.format(
            len(gds_collector.get_messages()), ))
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj


def main():
    args = sys.argv[1:]
    if len(args) == 1:
        parse(args[0])
    else:
        usage()


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()

RenameMappings_ = {
}

#
# Mapping of namespaces to types defined in them
# and the file in which each is defined.
# simpleTypes are marked "ST" and complexTypes "CT".
NamespaceToDefMappings_ = {'http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd': [('tcCpfCnpj',
                                                                              'Servico_Cancelar_justificativa_tipo_complexos.xsd',
                                                                              'CT'),
                                                                             ('tcEndereco',
                                                                              'Servico_Cancelar_justificativa_tipo_complexos.xsd',
                                                                              'CT'),
                                                                             ('tcContato',
                                                                              'Servico_Cancelar_justificativa_tipo_complexos.xsd',
                                                                              'CT'),
                                                                             ('tcIdentificacaoOrgaoGerador',
                                                                              'Servico_Cancelar_justificativa_tipo_complexos.xsd',
                                                                              'CT'),
                                                                             ('tcIdentificacaoRps',
                                                                              'Servico_Cancelar_justificativa_tipo_complexos.xsd',
                                                                              'CT'),
                                                                             ('tcIdentificacaoPrestador',
                                                                              'Servico_Cancelar_justificativa_tipo_complexos.xsd',
                                                                              'CT'),
                                                                             ('tcIdentificacaoTomador',
                                                                              'Servico_Cancelar_justificativa_tipo_complexos.xsd',
                                                                              'CT'),
                                                                             ('tcDadosTomador',
                                                                              'Servico_Cancelar_justificativa_tipo_complexos.xsd',
                                                                              'CT'),
                                                                             ('tcIdentificacaoIntermediarioServico',
                                                                              'Servico_Cancelar_justificativa_tipo_complexos.xsd',
                                                                              'CT'),
                                                                             ('tcValores',
                                                                              'Servico_Cancelar_justificativa_tipo_complexos.xsd',
                                                                              'CT'),
                                                                             ('tcDadosServico',
                                                                              'Servico_Cancelar_justificativa_tipo_complexos.xsd',
                                                                              'CT'),
                                                                             ('tcDadosConstrucaoCivil',
                                                                              'Servico_Cancelar_justificativa_tipo_complexos.xsd',
                                                                              'CT'),
                                                                             ('tcDadosPrestador',
                                                                              'Servico_Cancelar_justificativa_tipo_complexos.xsd',
                                                                              'CT'),
                                                                             ('tcAtividade',
                                                                              'Servico_Cancelar_justificativa_tipo_complexos.xsd',
                                                                              'CT'),
                                                                             ('tcSimplesNacional',
                                                                              'Servico_Cancelar_justificativa_tipo_complexos.xsd',
                                                                              'CT'),
                                                                             ('tcMei',
                                                                              'Servico_Cancelar_justificativa_tipo_complexos.xsd',
                                                                              'CT'),
                                                                             ('tcCnae',
                                                                              'Servico_Cancelar_justificativa_tipo_complexos.xsd',
                                                                              'CT'),
                                                                             ('tcNaturezaOperacao',
                                                                              'Servico_Cancelar_justificativa_tipo_complexos.xsd',
                                                                              'CT'),
                                                                             ('tcIdentificacaoContribuinte',
                                                                              'Servico_Cancelar_justificativa_tipo_complexos.xsd',
                                                                              'CT'),
                                                                             ('tcInfRps',
                                                                              'Servico_Cancelar_justificativa_tipo_complexos.xsd',
                                                                              'CT'),
                                                                             ('tcRps',
                                                                              'Servico_Cancelar_justificativa_tipo_complexos.xsd',
                                                                              'CT'),
                                                                             ('tcIdentificacaoNfse',
                                                                              'Servico_Cancelar_justificativa_tipo_complexos.xsd',
                                                                              'CT'),
                                                                             ('tcInfNfse',
                                                                              'Servico_Cancelar_justificativa_tipo_complexos.xsd',
                                                                              'CT'),
                                                                             ('tcNfse',
                                                                              'Servico_Cancelar_justificativa_tipo_complexos.xsd',
                                                                              'CT'),
                                                                             ('tcInfPedidoCancelamento',
                                                                              'Servico_Cancelar_justificativa_tipo_complexos.xsd',
                                                                              'CT'),
                                                                             ('tcPedidoCancelamento',
                                                                              'Servico_Cancelar_justificativa_tipo_complexos.xsd',
                                                                              'CT'),
                                                                             ('tcInfConfirmacaoCancelamento',
                                                                              'Servico_Cancelar_justificativa_tipo_complexos.xsd',
                                                                              'CT'),
                                                                             ('tcConfirmacaoCancelamento',
                                                                              'Servico_Cancelar_justificativa_tipo_complexos.xsd',
                                                                              'CT'),
                                                                             ('tcCancelamentoNfse',
                                                                              'Servico_Cancelar_justificativa_tipo_complexos.xsd',
                                                                              'CT'),
                                                                             ('tcInfSubstituicaoNfse',
                                                                              'Servico_Cancelar_justificativa_tipo_complexos.xsd',
                                                                              'CT'),
                                                                             ('tcSubstituicaoNfse',
                                                                              'Servico_Cancelar_justificativa_tipo_complexos.xsd',
                                                                              'CT'),
                                                                             ('tcCompNfse',
                                                                              'Servico_Cancelar_justificativa_tipo_complexos.xsd',
                                                                              'CT'),
                                                                             ('tcMensagemRetorno',
                                                                              'Servico_Cancelar_justificativa_tipo_complexos.xsd',
                                                                              'CT'),
                                                                             ('tcMensagemRetornoLote',
                                                                              'Servico_Cancelar_justificativa_tipo_complexos.xsd',
                                                                              'CT'),
                                                                             ('tcLoteRps',
                                                                              'Servico_Cancelar_justificativa_tipo_complexos.xsd',
                                                                              'CT')],
 'http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_simples.xsd': [('tsNumeroNfse',
                                                                            'tipos_simples.xsd',
                                                                            'ST'),
                                                                           ('tsCodigoVerificacao',
                                                                            'tipos_simples.xsd',
                                                                            'ST'),
                                                                           ('tsStatusRps',
                                                                            'tipos_simples.xsd',
                                                                            'ST'),
                                                                           ('tsStatusNfse',
                                                                            'tipos_simples.xsd',
                                                                            'ST'),
                                                                           ('tsNaturezaOperacao',
                                                                            'tipos_simples.xsd',
                                                                            'ST'),
                                                                           ('tsRegimeEspecialTributacao',
                                                                            'tipos_simples.xsd',
                                                                            'ST'),
                                                                           ('tsSimNao',
                                                                            'tipos_simples.xsd',
                                                                            'ST'),
                                                                           ('tsNumeroRps',
                                                                            'tipos_simples.xsd',
                                                                            'ST'),
                                                                           ('tsSerieRps',
                                                                            'tipos_simples.xsd',
                                                                            'ST'),
                                                                           ('tsTipoRps',
                                                                            'tipos_simples.xsd',
                                                                            'ST'),
                                                                           ('tsOutrasInformacoes',
                                                                            'tipos_simples.xsd',
                                                                            'ST'),
                                                                           ('tsValor',
                                                                            'tipos_simples.xsd',
                                                                            'ST'),
                                                                           ('tsItemListaServico',
                                                                            'tipos_simples.xsd',
                                                                            'ST'),
                                                                           ('tsCodigoCnae',
                                                                            'tipos_simples.xsd',
                                                                            'ST'),
                                                                           ('tsCodigoTributacao',
                                                                            'tipos_simples.xsd',
                                                                            'ST'),
                                                                           ('tsAliquota',
                                                                            'tipos_simples.xsd',
                                                                            'ST'),
                                                                           ('tsDiscriminacao',
                                                                            'tipos_simples.xsd',
                                                                            'ST'),
                                                                           ('tsCodigoMunicipioIbge',
                                                                            'tipos_simples.xsd',
                                                                            'ST'),
                                                                           ('tsInscricaoMunicipal',
                                                                            'tipos_simples.xsd',
                                                                            'ST'),
                                                                           ('tsRazaoSocial',
                                                                            'tipos_simples.xsd',
                                                                            'ST'),
                                                                           ('tsNomeFantasia',
                                                                            'tipos_simples.xsd',
                                                                            'ST'),
                                                                           ('tsCnpj',
                                                                            'tipos_simples.xsd',
                                                                            'ST'),
                                                                           ('tsEndereco',
                                                                            'tipos_simples.xsd',
                                                                            'ST'),
                                                                           ('tsNumeroEndereco',
                                                                            'tipos_simples.xsd',
                                                                            'ST'),
                                                                           ('tsComplementoEndereco',
                                                                            'tipos_simples.xsd',
                                                                            'ST'),
                                                                           ('tsBairro',
                                                                            'tipos_simples.xsd',
                                                                            'ST'),
                                                                           ('tsUf',
                                                                            'tipos_simples.xsd',
                                                                            'ST'),
                                                                           ('tsCep',
                                                                            'tipos_simples.xsd',
                                                                            'ST'),
                                                                           ('tsEmail',
                                                                            'tipos_simples.xsd',
                                                                            'ST'),
                                                                           ('tsTelefone',
                                                                            'tipos_simples.xsd',
                                                                            'ST'),
                                                                           ('tsCpf',
                                                                            'tipos_simples.xsd',
                                                                            'ST'),
                                                                           ('tsIndicacaoCpfCnpj',
                                                                            'tipos_simples.xsd',
                                                                            'ST'),
                                                                           ('tsCodigoObra',
                                                                            'tipos_simples.xsd',
                                                                            'ST'),
                                                                           ('tsArt',
                                                                            'tipos_simples.xsd',
                                                                            'ST'),
                                                                           ('tsNumeroLote',
                                                                            'tipos_simples.xsd',
                                                                            'ST'),
                                                                           ('tsNumeroProtocolo',
                                                                            'tipos_simples.xsd',
                                                                            'ST'),
                                                                           ('tsSituacaoLoteRps',
                                                                            'tipos_simples.xsd',
                                                                            'ST'),
                                                                           ('tsQuantidadeRps',
                                                                            'tipos_simples.xsd',
                                                                            'ST'),
                                                                           ('tsCodigoMensagemAlerta',
                                                                            'tipos_simples.xsd',
                                                                            'ST'),
                                                                           ('tsDescricaoMensagemAlerta',
                                                                            'tipos_simples.xsd',
                                                                            'ST'),
                                                                           ('tsCodigoCancelamentoNfse',
                                                                            'tipos_simples.xsd',
                                                                            'ST'),
                                                                           ('tsIdTag',
                                                                            'tipos_simples.xsd',
                                                                            'ST'),
                                                                           ('tsCompetencia',
                                                                            'tipos_simples.xsd',
                                                                            'ST')],
 'http://www.w3.org/2000/09/xmldsig#': [('CryptoBinary',
                                         'xmldsig-core-schema20020212.xsd',
                                         'ST'),
                                        ('DigestValueType',
                                         'xmldsig-core-schema20020212.xsd',
                                         'ST'),
                                        ('HMACOutputLengthType',
                                         'xmldsig-core-schema20020212.xsd',
                                         'ST'),
                                        ('SignatureType',
                                         'xmldsig-core-schema20020212.xsd',
                                         'CT'),
                                        ('SignatureValueType',
                                         'xmldsig-core-schema20020212.xsd',
                                         'CT'),
                                        ('SignedInfoType',
                                         'xmldsig-core-schema20020212.xsd',
                                         'CT'),
                                        ('CanonicalizationMethodType',
                                         'xmldsig-core-schema20020212.xsd',
                                         'CT'),
                                        ('SignatureMethodType',
                                         'xmldsig-core-schema20020212.xsd',
                                         'CT'),
                                        ('ReferenceType',
                                         'xmldsig-core-schema20020212.xsd',
                                         'CT'),
                                        ('TransformsType',
                                         'xmldsig-core-schema20020212.xsd',
                                         'CT'),
                                        ('TransformType',
                                         'xmldsig-core-schema20020212.xsd',
                                         'CT'),
                                        ('DigestMethodType',
                                         'xmldsig-core-schema20020212.xsd',
                                         'CT'),
                                        ('KeyInfoType',
                                         'xmldsig-core-schema20020212.xsd',
                                         'CT'),
                                        ('KeyValueType',
                                         'xmldsig-core-schema20020212.xsd',
                                         'CT'),
                                        ('RetrievalMethodType',
                                         'xmldsig-core-schema20020212.xsd',
                                         'CT'),
                                        ('X509DataType',
                                         'xmldsig-core-schema20020212.xsd',
                                         'CT'),
                                        ('X509IssuerSerialType',
                                         'xmldsig-core-schema20020212.xsd',
                                         'CT'),
                                        ('PGPDataType',
                                         'xmldsig-core-schema20020212.xsd',
                                         'CT'),
                                        ('SPKIDataType',
                                         'xmldsig-core-schema20020212.xsd',
                                         'CT'),
                                        ('ObjectType',
                                         'xmldsig-core-schema20020212.xsd',
                                         'CT'),
                                        ('ManifestType',
                                         'xmldsig-core-schema20020212.xsd',
                                         'CT'),
                                        ('SignaturePropertiesType',
                                         'xmldsig-core-schema20020212.xsd',
                                         'CT'),
                                        ('SignaturePropertyType',
                                         'xmldsig-core-schema20020212.xsd',
                                         'CT'),
                                        ('DSAKeyValueType',
                                         'xmldsig-core-schema20020212.xsd',
                                         'CT'),
                                        ('RSAKeyValueType',
                                         'xmldsig-core-schema20020212.xsd',
                                         'CT')]}

__all__ = [
    "ListaMensagemRetornoType",
    "ListaRpsType",
    "tcAtividade",
    "tcCancelamentoNfse",
    "tcCnae",
    "tcCompNfse",
    "tcConfirmacaoCancelamento",
    "tcContato",
    "tcCpfCnpj",
    "tcDadosConstrucaoCivil",
    "tcDadosPrestador",
    "tcDadosServico",
    "tcDadosTomador",
    "tcEndereco",
    "tcIdentificacaoContribuinte",
    "tcIdentificacaoIntermediarioServico",
    "tcIdentificacaoNfse",
    "tcIdentificacaoOrgaoGerador",
    "tcIdentificacaoPrestador",
    "tcIdentificacaoRps",
    "tcIdentificacaoTomador",
    "tcInfConfirmacaoCancelamento",
    "tcInfNfse",
    "tcInfPedidoCancelamento",
    "tcInfRps",
    "tcInfSubstituicaoNfse",
    "tcLoteRps",
    "tcMei",
    "tcMensagemRetorno",
    "tcMensagemRetornoLote",
    "tcNaturezaOperacao",
    "tcNfse",
    "tcPedidoCancelamento",
    "tcRps",
    "tcSimplesNacional",
    "tcSubstituicaoNfse",
    "tcValores"
]
