#!/usr/bin/perl -w

use HTML::Template;
use Time::Local;
use POSIX "strftime";
use strict;

my $NumImages = 48;

sub get_secs {

    my $dstr = shift;

    if ($dstr !~ /image_(\d*)_(\d*)_(\d*)_(\d*)_(\d*).jpg/) {
	return;
    }

    my ($year,$month,$day,$hour,$minute) = ($1,$2,$3,$4,$5);
    my $seconds = timegm(0,$minute,$hour,$day,$month-1,$year);

    $seconds;
}

sub get_str_from_secs {
    
    my $seconds = shift;
    
    my $timestr = strftime "%B %d %Y %T GMT", gmtime($seconds);

    $timestr;
}

chdir "/home/inyotech/ssec";

# open the html template
my $template = HTML::Template->new(filename => 'weather.tmpl',
				   loop_context_vars => 1);

my @files = `ls -1 images/image_*.jpg`;
my @display_files = ();
my $file;

sub by_date {
    # $a and $b automatically passed in
    return get_secs($a) <=> get_secs($b);
}

foreach $file (sort by_date @files) {
    chomp($file);
    push @display_files, $file;
}

if (($#display_files + 1) < $NumImages) {
    $NumImages = $#display_files + 1;
}

@display_files = @display_files[-$NumImages .. -1];

my $image_file;
my @dates = ();
my @names = ();
foreach $image_file (@display_files) {
    push @names, { IMAGE_NAME => $image_file };
    push @dates, { IMAGE_DATE => get_str_from_secs get_secs($image_file) };
}

$template->param(NUM_IMAGES => $NumImages);
$template->param(IMAGE_NAMES => \@names );
$template->param(IMAGE_DATES => \@dates );
$template->param(HOURS => $NumImages / 2 );

print "Content-Type: text/html\n\n";
print $template->output;
