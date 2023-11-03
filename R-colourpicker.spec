#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
#
Name     : R-colourpicker
Version  : 1.3.0
Release  : 52
URL      : https://cran.r-project.org/src/contrib/colourpicker_1.3.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/colourpicker_1.3.0.tar.gz
Summary  : A Colour Picker Tool for Shiny and for Selecting Colours in
Group    : Development/Tools
License  : MIT
Requires: R-ggplot2
Requires: R-htmltools
Requires: R-htmlwidgets
Requires: R-jsonlite
Requires: R-miniUI
Requires: R-shiny
Requires: R-shinyjs
BuildRequires : R-ggplot2
BuildRequires : R-htmltools
BuildRequires : R-htmlwidgets
BuildRequires : R-jsonlite
BuildRequires : R-miniUI
BuildRequires : R-shiny
BuildRequires : R-shinyjs
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
or Rmarkdown documents. The colour picker supports alpha opacity, custom
    colour palettes, and many more options. A Plot Colour Helper tool is
    available as an 'RStudio' Addin, which helps you pick colours to use in your
    plots. A more generic Colour Picker 'RStudio' Addin is also provided to let 
    you select colours to use in your R code.

%prep
%setup -q -n colourpicker
pushd ..
cp -a colourpicker buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1692632360

%install
export SOURCE_DATE_EPOCH=1692632360
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/colourpicker/DESCRIPTION
/usr/lib64/R/library/colourpicker/INDEX
/usr/lib64/R/library/colourpicker/LICENSE
/usr/lib64/R/library/colourpicker/Meta/Rd.rds
/usr/lib64/R/library/colourpicker/Meta/features.rds
/usr/lib64/R/library/colourpicker/Meta/hsearch.rds
/usr/lib64/R/library/colourpicker/Meta/links.rds
/usr/lib64/R/library/colourpicker/Meta/nsInfo.rds
/usr/lib64/R/library/colourpicker/Meta/package.rds
/usr/lib64/R/library/colourpicker/NAMESPACE
/usr/lib64/R/library/colourpicker/NEWS.md
/usr/lib64/R/library/colourpicker/R/colourpicker
/usr/lib64/R/library/colourpicker/R/colourpicker.rdb
/usr/lib64/R/library/colourpicker/R/colourpicker.rdx
/usr/lib64/R/library/colourpicker/examples/colourInput/app.R
/usr/lib64/R/library/colourpicker/examples/colourInput/www/app.css
/usr/lib64/R/library/colourpicker/examples/colourInput/www/github-gray-right.png
/usr/lib64/R/library/colourpicker/examples/colourInput/www/salvattore.min.js
/usr/lib64/R/library/colourpicker/gadgets/colourpicker/css/app.css
/usr/lib64/R/library/colourpicker/gadgets/colourpicker/css/plotHelper.css
/usr/lib64/R/library/colourpicker/gadgets/colourpicker/img/ajax-loader.gif
/usr/lib64/R/library/colourpicker/gadgets/colourpicker/js/shinyjs-funcs.js
/usr/lib64/R/library/colourpicker/help/AnIndex
/usr/lib64/R/library/colourpicker/help/aliases.rds
/usr/lib64/R/library/colourpicker/help/colourpicker.rdb
/usr/lib64/R/library/colourpicker/help/colourpicker.rdx
/usr/lib64/R/library/colourpicker/help/paths.rds
/usr/lib64/R/library/colourpicker/html/00Index.html
/usr/lib64/R/library/colourpicker/html/R.css
/usr/lib64/R/library/colourpicker/htmlwidgets/colourWidget.js
/usr/lib64/R/library/colourpicker/htmlwidgets/colourWidget.yaml
/usr/lib64/R/library/colourpicker/htmlwidgets/lib/jquery/jquery.min.js
/usr/lib64/R/library/colourpicker/img/colourPickerGadget.gif
/usr/lib64/R/library/colourpicker/img/colourinput.png
/usr/lib64/R/library/colourpicker/img/colourinputnew.PNG
/usr/lib64/R/library/colourpicker/img/colourpickerscrnshot.png
/usr/lib64/R/library/colourpicker/img/hex.png
/usr/lib64/R/library/colourpicker/img/limited-palette.png
/usr/lib64/R/library/colourpicker/img/plothelper-demo.gif
/usr/lib64/R/library/colourpicker/img/plothelper-demo.png
/usr/lib64/R/library/colourpicker/img/showColour.png
/usr/lib64/R/library/colourpicker/rstudio/addins.dcf
/usr/lib64/R/library/colourpicker/srcjs/input_binding_colour.js
/usr/lib64/R/library/colourpicker/www/shared/colourpicker/css/colourpicker.css
/usr/lib64/R/library/colourpicker/www/shared/colourpicker/css/colourpicker.min.css
/usr/lib64/R/library/colourpicker/www/shared/colourpicker/js/colourpicker.js
/usr/lib64/R/library/colourpicker/www/shared/colourpicker/js/colourpicker.min.js
