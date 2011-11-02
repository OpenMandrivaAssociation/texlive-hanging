Name:		texlive-hanging
Version:	1.2b
Release:	1
Summary:	Hanging paragraphs
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/hanging
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hanging.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hanging.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hanging.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The hanging package facilitates the typesetting of hanging
paragraphs. The package also enables typesetting with hanging
punctuation, by making punctuation characters active. This
facility is best suppressed (it can interfere with other
packages) -- there are package options for suppressing each
individual punctuation character. 'Real' attempts at hanging
punction should nowadays use the microtype package, which takes
advantage of the support offered in recent versions of pdfTeX.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/hanging/hanging.sty
%doc %{_texmfdistdir}/doc/latex/hanging/README
%doc %{_texmfdistdir}/doc/latex/hanging/hanging.pdf
#- source
%doc %{_texmfdistdir}/source/latex/hanging/hanging.dtx
%doc %{_texmfdistdir}/source/latex/hanging/hanging.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
