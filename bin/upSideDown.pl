#!/usr/bin/env perl
use strict;
use Text::UpsideDown;
use feature 'say';
no warnings;

say upside_down( "@ARGV" );
