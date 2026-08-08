%global tl_name cmgraded
%global tl_revision 79867

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0.1
Release:	%{tl_revision}.1
Summary:	Classic LaTeX look and feel in different grades of blackness
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/cmgraded
License:	ofl lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cmgraded.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cmgraded.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package contains OpenType and Type 1 (Adobe/PostScript) fonts named
"Computer Modern Graded" that have been generated from the original
"Computer Modern" fonts by Donald E. Knuth and TeX metrics by applying
different grades of "blackness" via Metafont that make the fonts
gradually darker, while keeping metrics intact and not turning a regular
weight font visually into a bold one. The fonts come in seven
increasingly black grades and can be easily used. Text fonts are
OpenType, while math is so far with Type 1 fonts, which means that text
can be fully tagged and thus made accessible. There are many more
options and angles to this package than meet the eye, just see the
documentation. Of course, the fonts can also be used outside of
TeX/LaTeX, with anything that speaks OpenType, including web content.

