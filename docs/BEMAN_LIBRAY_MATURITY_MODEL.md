<!--
SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
-->

# The Beman Library Maturity Model

This document specifies the Beman Library Maturity Model.
Its goal is to create awareness about the current status of Beman libraries.

## Introduction

### Changing this document

<!-- TODO: Maybe instead of duplicatind content from BEMAN_STANDARD.md#Changing-this-document here, we put a single section in root README.md -->

## Beman library maturity model

The Beman maturity model helps developers quickly assess the production readiness of Beman libraries by classifying them based on development phase and interface stability.

<img src="./img/beman-library-maturity-model.png">

### Under development and not yet ready for production use.
<img src="./img/logo-beman-library-under-development.png" style="width:5%; height:auto;"> These libraries may deviate from the Beman Standard due to incompleteness, lack of testing, inconsistencies with the specification, or other non-conformances. They are not recommended for production usage.

### Production ready. API may undergo changes.
<img src="./img/logo-beman-library-production-ready-api-may-undergo-changes.png" style="width:5%; height:auto;"> These Beman-compliant libraries are production-ready, fully implementing the target paper with complete testing and documentation. Users should be aware that future API changes are possible and that standardization is not guaranteed.

### Production ready. Stable API.
<img src="./img/logo-beman-library-production-ready-stable-api.png" style="width:5%; height:auto;"> These production-ready libraries offer stable, standardized APIs.  They are part of the C++ Standard and can be used as a polyfill for compilers lacking native support. Note that these libraries will be retired after two standardization cycles (6 years).

### Retired. No longer maintained or actively developed.
<img src="./img/logo-beman-library-retired.png" style="width:5%; height:auto;"> These libraries are not recommended for production use. They were completed and [Production ready. Stable API.](./BEMAN_LIBRAY_MATURITY_MODEL.md#production-ready-stable-api) at some point, but they are no longer developed or maintained, because they have been superseded by native compiler implementations.

### Dropped. Never got completed.
<img src="./img/logo-beman-library-dropped.png" style="width:5%; height:auto;"> These libraries should not be used for production. They were not got completed because they were not accepted into the the C++ Standard.
