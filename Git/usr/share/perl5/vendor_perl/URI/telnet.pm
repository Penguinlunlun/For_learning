package URI::telnet;

use strict;
use warnings;

our $VERSION = '5.19';

use parent 'URI::_login';

sub default_port { 23 }

1;