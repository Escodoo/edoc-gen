#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Generated Tue Sep 22 04:42:00 2020 by generateDS.py version 2.36.2.
# Python 3.6.9 (default, Nov  7 2019, 10:44:02)  [GCC 8.3.0]
#
# Command line options:
#   ('--no-collect-includes', '')
#   ('-f', '')
#   ('-o', '/root/generateds/edoc-gen/issnetlib/v1_00/servico_consultar_dados_cadastrais_resposta.py')
#
# Command line arguments:
#   servico_consultar_dados_cadastrais_resposta.xsd
#
# Command line:
#   /root/generateds/generateds-code/generateDS.py --no-collect-includes -f -o "/root/generateds/edoc-gen/issnetlib/v1_00/servico_consultar_dados_cadastrais_resposta.py" servico_consultar_dados_cadastrais_resposta.xsd
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


class ConsultarDadosCadastraisResposta(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, IdentificacaoPrestador=None, RazaoSocial=None, ListaCnae=None, ListaAtividade=None, ListaNaturezaOperacao=None, ListaSimplesNacional=None, ListaMei=None, PermiteDeducao=None, PermiteDescontoIncondicionado=None, PermiteDescontoCondicionado=None, ListaMensagemRetorno=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.IdentificacaoPrestador = IdentificacaoPrestador
        self.IdentificacaoPrestador_nsprefix_ = None
        self.RazaoSocial = RazaoSocial
        self.RazaoSocial_nsprefix_ = None
        self.ListaCnae = ListaCnae
        self.ListaCnae_nsprefix_ = None
        self.ListaAtividade = ListaAtividade
        self.ListaAtividade_nsprefix_ = None
        self.ListaNaturezaOperacao = ListaNaturezaOperacao
        self.ListaNaturezaOperacao_nsprefix_ = None
        self.ListaSimplesNacional = ListaSimplesNacional
        self.ListaSimplesNacional_nsprefix_ = None
        self.ListaMei = ListaMei
        self.ListaMei_nsprefix_ = None
        self.PermiteDeducao = PermiteDeducao
        self.PermiteDeducao_nsprefix_ = None
        self.PermiteDescontoIncondicionado = PermiteDescontoIncondicionado
        self.PermiteDescontoIncondicionado_nsprefix_ = None
        self.PermiteDescontoCondicionado = PermiteDescontoCondicionado
        self.PermiteDescontoCondicionado_nsprefix_ = None
        self.ListaMensagemRetorno = ListaMensagemRetorno
        self.ListaMensagemRetorno_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ConsultarDadosCadastraisResposta)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ConsultarDadosCadastraisResposta.subclass:
            return ConsultarDadosCadastraisResposta.subclass(*args_, **kwargs_)
        else:
            return ConsultarDadosCadastraisResposta(*args_, **kwargs_)
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
    def get_ListaCnae(self):
        return self.ListaCnae
    def set_ListaCnae(self, ListaCnae):
        self.ListaCnae = ListaCnae
    def get_ListaAtividade(self):
        return self.ListaAtividade
    def set_ListaAtividade(self, ListaAtividade):
        self.ListaAtividade = ListaAtividade
    def get_ListaNaturezaOperacao(self):
        return self.ListaNaturezaOperacao
    def set_ListaNaturezaOperacao(self, ListaNaturezaOperacao):
        self.ListaNaturezaOperacao = ListaNaturezaOperacao
    def get_ListaSimplesNacional(self):
        return self.ListaSimplesNacional
    def set_ListaSimplesNacional(self, ListaSimplesNacional):
        self.ListaSimplesNacional = ListaSimplesNacional
    def get_ListaMei(self):
        return self.ListaMei
    def set_ListaMei(self, ListaMei):
        self.ListaMei = ListaMei
    def get_PermiteDeducao(self):
        return self.PermiteDeducao
    def set_PermiteDeducao(self, PermiteDeducao):
        self.PermiteDeducao = PermiteDeducao
    def get_PermiteDescontoIncondicionado(self):
        return self.PermiteDescontoIncondicionado
    def set_PermiteDescontoIncondicionado(self, PermiteDescontoIncondicionado):
        self.PermiteDescontoIncondicionado = PermiteDescontoIncondicionado
    def get_PermiteDescontoCondicionado(self):
        return self.PermiteDescontoCondicionado
    def set_PermiteDescontoCondicionado(self, PermiteDescontoCondicionado):
        self.PermiteDescontoCondicionado = PermiteDescontoCondicionado
    def get_ListaMensagemRetorno(self):
        return self.ListaMensagemRetorno
    def set_ListaMensagemRetorno(self, ListaMensagemRetorno):
        self.ListaMensagemRetorno = ListaMensagemRetorno
    def hasContent_(self):
        if (
            self.IdentificacaoPrestador is not None or
            self.RazaoSocial is not None or
            self.ListaCnae is not None or
            self.ListaAtividade is not None or
            self.ListaNaturezaOperacao is not None or
            self.ListaSimplesNacional is not None or
            self.ListaMei is not None or
            self.PermiteDeducao is not None or
            self.PermiteDescontoIncondicionado is not None or
            self.PermiteDescontoCondicionado is not None or
            self.ListaMensagemRetorno is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:tc="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd"  xmlns:ts="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_simples.xsd"  xmlns:None="http://www.issnetonline.com.br/webserviceabrasf/vsd/servico_consultar_dados_cadastrais_resposta.xsd" ', name_='ConsultarDadosCadastraisResposta', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ConsultarDadosCadastraisResposta')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ConsultarDadosCadastraisResposta':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ConsultarDadosCadastraisResposta')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ConsultarDadosCadastraisResposta', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ConsultarDadosCadastraisResposta'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:tc="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd"  xmlns:ts="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_simples.xsd"  xmlns:None="http://www.issnetonline.com.br/webserviceabrasf/vsd/servico_consultar_dados_cadastrais_resposta.xsd" ', name_='ConsultarDadosCadastraisResposta', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.IdentificacaoPrestador is not None:
            namespaceprefix_ = self.IdentificacaoPrestador_nsprefix_ + ':' if (UseCapturedNS_ and self.IdentificacaoPrestador_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sIdentificacaoPrestador>%s</%sIdentificacaoPrestador>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.IdentificacaoPrestador), input_name='IdentificacaoPrestador')), namespaceprefix_ , eol_))
        if self.RazaoSocial is not None:
            namespaceprefix_ = self.RazaoSocial_nsprefix_ + ':' if (UseCapturedNS_ and self.RazaoSocial_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sRazaoSocial>%s</%sRazaoSocial>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.RazaoSocial), input_name='RazaoSocial')), namespaceprefix_ , eol_))
        if self.ListaCnae is not None:
            namespaceprefix_ = self.ListaCnae_nsprefix_ + ':' if (UseCapturedNS_ and self.ListaCnae_nsprefix_) else ''
            self.ListaCnae.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ListaCnae', pretty_print=pretty_print)
        if self.ListaAtividade is not None:
            namespaceprefix_ = self.ListaAtividade_nsprefix_ + ':' if (UseCapturedNS_ and self.ListaAtividade_nsprefix_) else ''
            self.ListaAtividade.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ListaAtividade', pretty_print=pretty_print)
        if self.ListaNaturezaOperacao is not None:
            namespaceprefix_ = self.ListaNaturezaOperacao_nsprefix_ + ':' if (UseCapturedNS_ and self.ListaNaturezaOperacao_nsprefix_) else ''
            self.ListaNaturezaOperacao.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ListaNaturezaOperacao', pretty_print=pretty_print)
        if self.ListaSimplesNacional is not None:
            namespaceprefix_ = self.ListaSimplesNacional_nsprefix_ + ':' if (UseCapturedNS_ and self.ListaSimplesNacional_nsprefix_) else ''
            self.ListaSimplesNacional.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ListaSimplesNacional', pretty_print=pretty_print)
        if self.ListaMei is not None:
            namespaceprefix_ = self.ListaMei_nsprefix_ + ':' if (UseCapturedNS_ and self.ListaMei_nsprefix_) else ''
            self.ListaMei.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ListaMei', pretty_print=pretty_print)
        if self.PermiteDeducao is not None:
            namespaceprefix_ = self.PermiteDeducao_nsprefix_ + ':' if (UseCapturedNS_ and self.PermiteDeducao_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sPermiteDeducao>%s</%sPermiteDeducao>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.PermiteDeducao), input_name='PermiteDeducao')), namespaceprefix_ , eol_))
        if self.PermiteDescontoIncondicionado is not None:
            namespaceprefix_ = self.PermiteDescontoIncondicionado_nsprefix_ + ':' if (UseCapturedNS_ and self.PermiteDescontoIncondicionado_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sPermiteDescontoIncondicionado>%s</%sPermiteDescontoIncondicionado>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.PermiteDescontoIncondicionado), input_name='PermiteDescontoIncondicionado')), namespaceprefix_ , eol_))
        if self.PermiteDescontoCondicionado is not None:
            namespaceprefix_ = self.PermiteDescontoCondicionado_nsprefix_ + ':' if (UseCapturedNS_ and self.PermiteDescontoCondicionado_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sPermiteDescontoCondicionado>%s</%sPermiteDescontoCondicionado>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.PermiteDescontoCondicionado), input_name='PermiteDescontoCondicionado')), namespaceprefix_ , eol_))
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
        if nodeName_ == 'IdentificacaoPrestador':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'IdentificacaoPrestador')
            value_ = self.gds_validate_string(value_, node, 'IdentificacaoPrestador')
            self.IdentificacaoPrestador = value_
            self.IdentificacaoPrestador_nsprefix_ = child_.prefix
        elif nodeName_ == 'RazaoSocial':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'RazaoSocial')
            value_ = self.gds_validate_string(value_, node, 'RazaoSocial')
            self.RazaoSocial = value_
            self.RazaoSocial_nsprefix_ = child_.prefix
        elif nodeName_ == 'ListaCnae':
            obj_ = ListaCnaeType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ListaCnae = obj_
            obj_.original_tagname_ = 'ListaCnae'
        elif nodeName_ == 'ListaAtividade':
            obj_ = ListaAtividadeType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ListaAtividade = obj_
            obj_.original_tagname_ = 'ListaAtividade'
        elif nodeName_ == 'ListaNaturezaOperacao':
            obj_ = ListaNaturezaOperacaoType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ListaNaturezaOperacao = obj_
            obj_.original_tagname_ = 'ListaNaturezaOperacao'
        elif nodeName_ == 'ListaSimplesNacional':
            obj_ = ListaSimplesNacionalType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ListaSimplesNacional = obj_
            obj_.original_tagname_ = 'ListaSimplesNacional'
        elif nodeName_ == 'ListaMei':
            obj_ = ListaMeiType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ListaMei = obj_
            obj_.original_tagname_ = 'ListaMei'
        elif nodeName_ == 'PermiteDeducao':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'PermiteDeducao')
            value_ = self.gds_validate_string(value_, node, 'PermiteDeducao')
            self.PermiteDeducao = value_
            self.PermiteDeducao_nsprefix_ = child_.prefix
        elif nodeName_ == 'PermiteDescontoIncondicionado':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'PermiteDescontoIncondicionado')
            value_ = self.gds_validate_string(value_, node, 'PermiteDescontoIncondicionado')
            self.PermiteDescontoIncondicionado = value_
            self.PermiteDescontoIncondicionado_nsprefix_ = child_.prefix
        elif nodeName_ == 'PermiteDescontoCondicionado':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'PermiteDescontoCondicionado')
            value_ = self.gds_validate_string(value_, node, 'PermiteDescontoCondicionado')
            self.PermiteDescontoCondicionado = value_
            self.PermiteDescontoCondicionado_nsprefix_ = child_.prefix
        elif nodeName_ == 'ListaMensagemRetorno':
            obj_ = ListaMensagemRetornoType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ListaMensagemRetorno = obj_
            obj_.original_tagname_ = 'ListaMensagemRetorno'
# end class ConsultarDadosCadastraisResposta


class ListaCnaeType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Cnae=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if Cnae is None:
            self.Cnae = []
        else:
            self.Cnae = Cnae
        self.Cnae_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ListaCnaeType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ListaCnaeType.subclass:
            return ListaCnaeType.subclass(*args_, **kwargs_)
        else:
            return ListaCnaeType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Cnae(self):
        return self.Cnae
    def set_Cnae(self, Cnae):
        self.Cnae = Cnae
    def add_Cnae(self, value):
        self.Cnae.append(value)
    def insert_Cnae_at(self, index, value):
        self.Cnae.insert(index, value)
    def replace_Cnae_at(self, index, value):
        self.Cnae[index] = value
    def hasContent_(self):
        if (
            self.Cnae
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:tc="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd" ', name_='ListaCnaeType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ListaCnaeType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ListaCnaeType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ListaCnaeType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ListaCnaeType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ListaCnaeType'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:tc="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd" ', name_='ListaCnaeType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Cnae_ in self.Cnae:
            namespaceprefix_ = self.Cnae_nsprefix_ + ':' if (UseCapturedNS_ and self.Cnae_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCnae>%s</%sCnae>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(Cnae_), input_name='Cnae')), namespaceprefix_ , eol_))
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
        if nodeName_ == 'Cnae':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Cnae')
            value_ = self.gds_validate_string(value_, node, 'Cnae')
            self.Cnae.append(value_)
            self.Cnae_nsprefix_ = child_.prefix
# end class ListaCnaeType


class ListaAtividadeType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Atividade=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if Atividade is None:
            self.Atividade = []
        else:
            self.Atividade = Atividade
        self.Atividade_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ListaAtividadeType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ListaAtividadeType.subclass:
            return ListaAtividadeType.subclass(*args_, **kwargs_)
        else:
            return ListaAtividadeType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Atividade(self):
        return self.Atividade
    def set_Atividade(self, Atividade):
        self.Atividade = Atividade
    def add_Atividade(self, value):
        self.Atividade.append(value)
    def insert_Atividade_at(self, index, value):
        self.Atividade.insert(index, value)
    def replace_Atividade_at(self, index, value):
        self.Atividade[index] = value
    def hasContent_(self):
        if (
            self.Atividade
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:tc="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd" ', name_='ListaAtividadeType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ListaAtividadeType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ListaAtividadeType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ListaAtividadeType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ListaAtividadeType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ListaAtividadeType'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:tc="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd" ', name_='ListaAtividadeType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Atividade_ in self.Atividade:
            namespaceprefix_ = self.Atividade_nsprefix_ + ':' if (UseCapturedNS_ and self.Atividade_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sAtividade>%s</%sAtividade>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(Atividade_), input_name='Atividade')), namespaceprefix_ , eol_))
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
        if nodeName_ == 'Atividade':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Atividade')
            value_ = self.gds_validate_string(value_, node, 'Atividade')
            self.Atividade.append(value_)
            self.Atividade_nsprefix_ = child_.prefix
# end class ListaAtividadeType


class ListaNaturezaOperacaoType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, NaturezaOperacao=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if NaturezaOperacao is None:
            self.NaturezaOperacao = []
        else:
            self.NaturezaOperacao = NaturezaOperacao
        self.NaturezaOperacao_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ListaNaturezaOperacaoType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ListaNaturezaOperacaoType.subclass:
            return ListaNaturezaOperacaoType.subclass(*args_, **kwargs_)
        else:
            return ListaNaturezaOperacaoType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_NaturezaOperacao(self):
        return self.NaturezaOperacao
    def set_NaturezaOperacao(self, NaturezaOperacao):
        self.NaturezaOperacao = NaturezaOperacao
    def add_NaturezaOperacao(self, value):
        self.NaturezaOperacao.append(value)
    def insert_NaturezaOperacao_at(self, index, value):
        self.NaturezaOperacao.insert(index, value)
    def replace_NaturezaOperacao_at(self, index, value):
        self.NaturezaOperacao[index] = value
    def hasContent_(self):
        if (
            self.NaturezaOperacao
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:tc="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd" ', name_='ListaNaturezaOperacaoType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ListaNaturezaOperacaoType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ListaNaturezaOperacaoType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ListaNaturezaOperacaoType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ListaNaturezaOperacaoType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ListaNaturezaOperacaoType'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:tc="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd" ', name_='ListaNaturezaOperacaoType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for NaturezaOperacao_ in self.NaturezaOperacao:
            namespaceprefix_ = self.NaturezaOperacao_nsprefix_ + ':' if (UseCapturedNS_ and self.NaturezaOperacao_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sNaturezaOperacao>%s</%sNaturezaOperacao>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(NaturezaOperacao_), input_name='NaturezaOperacao')), namespaceprefix_ , eol_))
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
        if nodeName_ == 'NaturezaOperacao':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'NaturezaOperacao')
            value_ = self.gds_validate_string(value_, node, 'NaturezaOperacao')
            self.NaturezaOperacao.append(value_)
            self.NaturezaOperacao_nsprefix_ = child_.prefix
# end class ListaNaturezaOperacaoType


class ListaSimplesNacionalType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, SimplesNacional=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.SimplesNacional = SimplesNacional
        self.SimplesNacional_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ListaSimplesNacionalType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ListaSimplesNacionalType.subclass:
            return ListaSimplesNacionalType.subclass(*args_, **kwargs_)
        else:
            return ListaSimplesNacionalType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_SimplesNacional(self):
        return self.SimplesNacional
    def set_SimplesNacional(self, SimplesNacional):
        self.SimplesNacional = SimplesNacional
    def hasContent_(self):
        if (
            self.SimplesNacional is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:tc="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd" ', name_='ListaSimplesNacionalType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ListaSimplesNacionalType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ListaSimplesNacionalType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ListaSimplesNacionalType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ListaSimplesNacionalType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ListaSimplesNacionalType'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:tc="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd" ', name_='ListaSimplesNacionalType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.SimplesNacional is not None:
            namespaceprefix_ = self.SimplesNacional_nsprefix_ + ':' if (UseCapturedNS_ and self.SimplesNacional_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sSimplesNacional>%s</%sSimplesNacional>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.SimplesNacional), input_name='SimplesNacional')), namespaceprefix_ , eol_))
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
        if nodeName_ == 'SimplesNacional':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'SimplesNacional')
            value_ = self.gds_validate_string(value_, node, 'SimplesNacional')
            self.SimplesNacional = value_
            self.SimplesNacional_nsprefix_ = child_.prefix
# end class ListaSimplesNacionalType


class ListaMeiType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Mei=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Mei = Mei
        self.Mei_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ListaMeiType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ListaMeiType.subclass:
            return ListaMeiType.subclass(*args_, **kwargs_)
        else:
            return ListaMeiType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Mei(self):
        return self.Mei
    def set_Mei(self, Mei):
        self.Mei = Mei
    def hasContent_(self):
        if (
            self.Mei is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:tc="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd" ', name_='ListaMeiType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ListaMeiType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ListaMeiType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ListaMeiType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ListaMeiType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ListaMeiType'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:tc="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd" ', name_='ListaMeiType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Mei is not None:
            namespaceprefix_ = self.Mei_nsprefix_ + ':' if (UseCapturedNS_ and self.Mei_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sMei>%s</%sMei>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Mei), input_name='Mei')), namespaceprefix_ , eol_))
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
# end class ListaMeiType


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
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:tc="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd" ', name_='ListaMensagemRetornoType', pretty_print=True):
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
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:tc="http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd" ', name_='ListaMensagemRetornoType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for MensagemRetorno_ in self.MensagemRetorno:
            namespaceprefix_ = self.MensagemRetorno_nsprefix_ + ':' if (UseCapturedNS_ and self.MensagemRetorno_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sMensagemRetorno>%s</%sMensagemRetorno>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(MensagemRetorno_), input_name='MensagemRetorno')), namespaceprefix_ , eol_))
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
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'MensagemRetorno')
            value_ = self.gds_validate_string(value_, node, 'MensagemRetorno')
            self.MensagemRetorno.append(value_)
            self.MensagemRetorno_nsprefix_ = child_.prefix
# end class ListaMensagemRetornoType


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
        rootTag = 'ConsultarDadosCadastraisResposta'
        rootClass = ConsultarDadosCadastraisResposta
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
        rootTag = 'ConsultarDadosCadastraisResposta'
        rootClass = ConsultarDadosCadastraisResposta
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
        rootTag = 'ConsultarDadosCadastraisResposta'
        rootClass = ConsultarDadosCadastraisResposta
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
        rootTag = 'ConsultarDadosCadastraisResposta'
        rootClass = ConsultarDadosCadastraisResposta
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        sys.stdout.write('#from servico_consultar_dados_cadastrais_resposta import *\n\n')
        sys.stdout.write('import servico_consultar_dados_cadastrais_resposta as model_\n\n')
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
NamespaceToDefMappings_ = {'http://www.issnetonline.com.br/webserviceabrasf/vsd/servico_consultar_dados_cadastrais_resposta.xsd': [],
 'http://www.issnetonline.com.br/webserviceabrasf/vsd/tipos_complexos.xsd': [('tcCpfCnpj',
                                                                              'tipos_complexos.xsd',
                                                                              'CT'),
                                                                             ('tcEndereco',
                                                                              'tipos_complexos.xsd',
                                                                              'CT'),
                                                                             ('tcContato',
                                                                              'tipos_complexos.xsd',
                                                                              'CT'),
                                                                             ('tcIdentificacaoOrgaoGerador',
                                                                              'tipos_complexos.xsd',
                                                                              'CT'),
                                                                             ('tcIdentificacaoRps',
                                                                              'tipos_complexos.xsd',
                                                                              'CT'),
                                                                             ('tcIdentificacaoPrestador',
                                                                              'tipos_complexos.xsd',
                                                                              'CT'),
                                                                             ('tcIdentificacaoTomador',
                                                                              'tipos_complexos.xsd',
                                                                              'CT'),
                                                                             ('tcDadosTomador',
                                                                              'tipos_complexos.xsd',
                                                                              'CT'),
                                                                             ('tcIdentificacaoIntermediarioServico',
                                                                              'tipos_complexos.xsd',
                                                                              'CT'),
                                                                             ('tcValores',
                                                                              'tipos_complexos.xsd',
                                                                              'CT'),
                                                                             ('tcDadosServico',
                                                                              'tipos_complexos.xsd',
                                                                              'CT'),
                                                                             ('tcDadosConstrucaoCivil',
                                                                              'tipos_complexos.xsd',
                                                                              'CT'),
                                                                             ('tcDadosPrestador',
                                                                              'tipos_complexos.xsd',
                                                                              'CT'),
                                                                             ('tcInfRps',
                                                                              'tipos_complexos.xsd',
                                                                              'CT'),
                                                                             ('tcRps',
                                                                              'tipos_complexos.xsd',
                                                                              'CT'),
                                                                             ('tcIdentificacaoNfse',
                                                                              'tipos_complexos.xsd',
                                                                              'CT'),
                                                                             ('tcInfNfse',
                                                                              'tipos_complexos.xsd',
                                                                              'CT'),
                                                                             ('tcNfse',
                                                                              'tipos_complexos.xsd',
                                                                              'CT'),
                                                                             ('tcInfPedidoCancelamento',
                                                                              'tipos_complexos.xsd',
                                                                              'CT'),
                                                                             ('tcPedidoCancelamento',
                                                                              'tipos_complexos.xsd',
                                                                              'CT'),
                                                                             ('tcInfConfirmacaoCancelamento',
                                                                              'tipos_complexos.xsd',
                                                                              'CT'),
                                                                             ('tcConfirmacaoCancelamento',
                                                                              'tipos_complexos.xsd',
                                                                              'CT'),
                                                                             ('tcCancelamentoNfse',
                                                                              'tipos_complexos.xsd',
                                                                              'CT'),
                                                                             ('tcInfSubstituicaoNfse',
                                                                              'tipos_complexos.xsd',
                                                                              'CT'),
                                                                             ('tcSubstituicaoNfse',
                                                                              'tipos_complexos.xsd',
                                                                              'CT'),
                                                                             ('tcCompNfse',
                                                                              'tipos_complexos.xsd',
                                                                              'CT'),
                                                                             ('tcMensagemRetorno',
                                                                              'tipos_complexos.xsd',
                                                                              'CT'),
                                                                             ('tcMensagemRetornoLote',
                                                                              'tipos_complexos.xsd',
                                                                              'CT'),
                                                                             ('tcLoteRps',
                                                                              'tipos_complexos.xsd',
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
    "ConsultarDadosCadastraisResposta",
    "ListaAtividadeType",
    "ListaCnaeType",
    "ListaMeiType",
    "ListaMensagemRetornoType",
    "ListaNaturezaOperacaoType",
    "ListaSimplesNacionalType"
]
