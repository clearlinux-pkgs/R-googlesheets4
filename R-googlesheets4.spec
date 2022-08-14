#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-googlesheets4
Version  : 1.0.1
Release  : 7
URL      : https://cran.r-project.org/src/contrib/googlesheets4_1.0.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/googlesheets4_1.0.1.tar.gz
Summary  : Access Google Sheets using the Sheets API V4
Group    : Development/Tools
License  : MIT
Requires: R-cellranger
Requires: R-cli
Requires: R-curl
Requires: R-gargle
Requires: R-glue
Requires: R-googledrive
Requires: R-httr
Requires: R-ids
Requires: R-magrittr
Requires: R-purrr
Requires: R-rematch2
Requires: R-rlang
Requires: R-tibble
Requires: R-vctrs
BuildRequires : R-cellranger
BuildRequires : R-cli
BuildRequires : R-curl
BuildRequires : R-gargle
BuildRequires : R-glue
BuildRequires : R-googledrive
BuildRequires : R-httr
BuildRequires : R-ids
BuildRequires : R-magrittr
BuildRequires : R-purrr
BuildRequires : R-rematch2
BuildRequires : R-rlang
BuildRequires : R-tibble
BuildRequires : R-vctrs
BuildRequires : buildreq-R

%description
# googlesheets4 <a href='https:/googlesheets4.tidyverse.org'><img src='man/figures/logo.png' align="right" height="138.5" /></a>

%prep
%setup -q -n googlesheets4
cd %{_builddir}/googlesheets4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1660519256

%install
export SOURCE_DATE_EPOCH=1660519256
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/googlesheets4/DESCRIPTION
/usr/lib64/R/library/googlesheets4/INDEX
/usr/lib64/R/library/googlesheets4/LICENSE
/usr/lib64/R/library/googlesheets4/Meta/Rd.rds
/usr/lib64/R/library/googlesheets4/Meta/features.rds
/usr/lib64/R/library/googlesheets4/Meta/hsearch.rds
/usr/lib64/R/library/googlesheets4/Meta/links.rds
/usr/lib64/R/library/googlesheets4/Meta/nsInfo.rds
/usr/lib64/R/library/googlesheets4/Meta/package.rds
/usr/lib64/R/library/googlesheets4/NAMESPACE
/usr/lib64/R/library/googlesheets4/NEWS.md
/usr/lib64/R/library/googlesheets4/R/googlesheets4
/usr/lib64/R/library/googlesheets4/R/googlesheets4.rdb
/usr/lib64/R/library/googlesheets4/R/googlesheets4.rdx
/usr/lib64/R/library/googlesheets4/R/sysdata.rdb
/usr/lib64/R/library/googlesheets4/R/sysdata.rdx
/usr/lib64/R/library/googlesheets4/WORDLIST
/usr/lib64/R/library/googlesheets4/extdata/example_and_test_sheets.csv
/usr/lib64/R/library/googlesheets4/extdata/fake-oauth-client-id-and-secret.json
/usr/lib64/R/library/googlesheets4/help/AnIndex
/usr/lib64/R/library/googlesheets4/help/aliases.rds
/usr/lib64/R/library/googlesheets4/help/figures/lifecycle-archived.svg
/usr/lib64/R/library/googlesheets4/help/figures/lifecycle-defunct.svg
/usr/lib64/R/library/googlesheets4/help/figures/lifecycle-deprecated.svg
/usr/lib64/R/library/googlesheets4/help/figures/lifecycle-experimental.svg
/usr/lib64/R/library/googlesheets4/help/figures/lifecycle-maturing.svg
/usr/lib64/R/library/googlesheets4/help/figures/lifecycle-questioning.svg
/usr/lib64/R/library/googlesheets4/help/figures/lifecycle-retired.svg
/usr/lib64/R/library/googlesheets4/help/figures/lifecycle-soft-deprecated.svg
/usr/lib64/R/library/googlesheets4/help/figures/lifecycle-stable.svg
/usr/lib64/R/library/googlesheets4/help/figures/logo.png
/usr/lib64/R/library/googlesheets4/help/googlesheets4.rdb
/usr/lib64/R/library/googlesheets4/help/googlesheets4.rdx
/usr/lib64/R/library/googlesheets4/help/paths.rds
/usr/lib64/R/library/googlesheets4/html/00Index.html
/usr/lib64/R/library/googlesheets4/html/R.css
/usr/lib64/R/library/googlesheets4/secret/googlesheets4-docs.json
/usr/lib64/R/library/googlesheets4/secret/googlesheets4-testing.json
/usr/lib64/R/library/googlesheets4/tests/spelling.R
/usr/lib64/R/library/googlesheets4/tests/testthat.R
/usr/lib64/R/library/googlesheets4/tests/testthat/_snaps/range_read.md
/usr/lib64/R/library/googlesheets4/tests/testthat/_snaps/schemas.md
/usr/lib64/R/library/googlesheets4/tests/testthat/_snaps/sheet_add.md
/usr/lib64/R/library/googlesheets4/tests/testthat/_snaps/sheets_id-class.md
/usr/lib64/R/library/googlesheets4/tests/testthat/_snaps/utils-ui.md
/usr/lib64/R/library/googlesheets4/tests/testthat/helper.R
/usr/lib64/R/library/googlesheets4/tests/testthat/ref/dribble.rds
/usr/lib64/R/library/googlesheets4/tests/testthat/ref/googlesheets4-cell-tests.rds
/usr/lib64/R/library/googlesheets4/tests/testthat/test-aaa.R
/usr/lib64/R/library/googlesheets4/tests/testthat/test-ctype.R
/usr/lib64/R/library/googlesheets4/tests/testthat/test-get_cells.R
/usr/lib64/R/library/googlesheets4/tests/testthat/test-gs4_endpoints.R
/usr/lib64/R/library/googlesheets4/tests/testthat/test-gs4_example.R
/usr/lib64/R/library/googlesheets4/tests/testthat/test-gs4_find.R
/usr/lib64/R/library/googlesheets4/tests/testthat/test-gs4_fodder.R
/usr/lib64/R/library/googlesheets4/tests/testthat/test-gs4_formula.R
/usr/lib64/R/library/googlesheets4/tests/testthat/test-make_column.R
/usr/lib64/R/library/googlesheets4/tests/testthat/test-range_autofit.R
/usr/lib64/R/library/googlesheets4/tests/testthat/test-range_delete.R
/usr/lib64/R/library/googlesheets4/tests/testthat/test-range_flood.R
/usr/lib64/R/library/googlesheets4/tests/testthat/test-range_read.R
/usr/lib64/R/library/googlesheets4/tests/testthat/test-range_read_cells.R
/usr/lib64/R/library/googlesheets4/tests/testthat/test-range_spec.R
/usr/lib64/R/library/googlesheets4/tests/testthat/test-range_speedread.R
/usr/lib64/R/library/googlesheets4/tests/testthat/test-range_write.R
/usr/lib64/R/library/googlesheets4/tests/testthat/test-rectangle.R
/usr/lib64/R/library/googlesheets4/tests/testthat/test-request_generate.R
/usr/lib64/R/library/googlesheets4/tests/testthat/test-schema_CellData.R
/usr/lib64/R/library/googlesheets4/tests/testthat/test-schema_GridCoordinate.R
/usr/lib64/R/library/googlesheets4/tests/testthat/test-schema_GridRange.R
/usr/lib64/R/library/googlesheets4/tests/testthat/test-schemas.R
/usr/lib64/R/library/googlesheets4/tests/testthat/test-sheet_add.R
/usr/lib64/R/library/googlesheets4/tests/testthat/test-sheet_append.R
/usr/lib64/R/library/googlesheets4/tests/testthat/test-sheet_copy.R
/usr/lib64/R/library/googlesheets4/tests/testthat/test-sheet_delete.R
/usr/lib64/R/library/googlesheets4/tests/testthat/test-sheet_relocate.R
/usr/lib64/R/library/googlesheets4/tests/testthat/test-sheet_rename.R
/usr/lib64/R/library/googlesheets4/tests/testthat/test-sheet_resize.R
/usr/lib64/R/library/googlesheets4/tests/testthat/test-sheet_write.R
/usr/lib64/R/library/googlesheets4/tests/testthat/test-sheets_id-class.R
/usr/lib64/R/library/googlesheets4/tests/testthat/test-utils-cell-ranges.R
/usr/lib64/R/library/googlesheets4/tests/testthat/test-utils-sheet.R
/usr/lib64/R/library/googlesheets4/tests/testthat/test-utils-ui.R
/usr/lib64/R/library/googlesheets4/tests/testthat/test-utils.R
