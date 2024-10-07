# The Beman Standard

<!--
SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception

Copyright (c) 2024 David Sankel <dsankel@boost.org>
-->

This document specifies rules and recommendations for Beman project libraries.
Its goal is to create consistency facilitating the evaluation of, and
contribution to Beman libraries.

## Introduction

### Core principles

This standard is driven by four core principles:

1. **[CORE.QUALITY] Highest quality**. Standards track libraries impact
   countless engineers and, consequently, should be of the highest quality.
2. **[CORE.PRODUCTION_READY] Production-ready**. Production feedback
   necessitates reliable, well-documented software.
3. **[CORE.INDUSTRY_STANDARD] Industry standard technology**. Where there's
   industry consensus on best practices, we should take advantage. Innovation in
   tooling and style is not our purpose.
4. **[CORE.INCLUSIVE] Welcoming and inclusive community**. Broad, useful
   feedback requires an unobstructed path for using, reviewing, and
   contributing to Beman libraries. This principle encompasses ergonomics,
   cross-industry participation, and cultural accommodation.

### Changing this document

This is a living document that adapts to evolving best practices and community
needs. To make changes:

1. Create a [discourse topic](https://discourse.boost.org) detailing the change
   and how it aligns with the core principles.
2. After some community discussion, create a PR with the actual change on
   [GitHub](https://github.com/beman-project/beman) with a *leads question*
   label. The PR should also link to the discourse topic.
3. Continue discussions on the PR and discourse topic.
4. Await a leads a decision based on the community feedback.

### Conventions

This standard consists of entries that include an all-caps, dot-separated
identifier for referencing.

With the exception of the core principles, these entries are either rules or
recommendations.

- **Requirements** must be followed in order to conform to this standard. These entries
  are prefixed by "REQUIREMENT:".
- **Recommendations** should be followed in general, but specific circumstances
  may make this a less-than-ideal choice. Libraries not following a specific
  recommendation can still conform to this standard. These entries are prefixed
  by "RECOMMENDATION:".

## License

**[LICENSE.APPROVED]** REQUIREMENT: All Beman libraries must be licensed
under an approved license. These are:

1. [Apache License v2.0 with LLVM Exceptions](https://llvm.org/LICENSE.txt)
2. [Boost Software License 1.0](https://www.boost.org/LICENSE_1_0.txt)
3. [The MIT License](https://opensource.org/license/mit)

**[LICENSE.APACHE_LLVM]** RECOMMENDATION: All Beman libraries should be licensed
under the [Apache License v2.0 with LLVM
Exceptions](https://llvm.org/LICENSE.txt).

**[LICENSE.CRITERIA]** REQUIREMENT: All approved licenses must meet the
following requirements:

1. Simple to read and understand.
2. Permission without fee to copy, use and modify the software for any
   use (commercial and non-commercial).
3. Requires that the license appears on all copies of the software source code.
4. Must not require that the license appears with executables or other binary
   uses of the library.
5. Must not require that the source code be available for execution or other
   binary uses of the library.

## General

**[LIBRARY.NAMES]** RECOMMENDATION: Beman libraries names begin with `beman.`
followed by an `snake_case` short name.

Examples are beman.smart_pointer and beman.sender_receiver.

**[REPOSITORY.NAME]** RECOMMENDATION: The repository should be named after the
library name excluding the `beman.` prefix.

For example, a beman.smart_pointer library's repository should be named
`smart_pointer`.

**[REPOSITORY.CODEOWNERS]** REQUIREMENT: There must be a `.github/CODEOWNERS` file at the
repository's root with relevant set of codeowners.

## Top-level

The top-level of a Beman library repository must consist of few required files, 
which are listed below.

**[TOPLEVEL.CMAKE]** REQUIREMENT: There must be a `CMakeLists.txt` file at the repository's root
that builds and tests (via. CTest) the library.

**[TOPLEVEL.LICENSE]** REQUIREMENT: There must be a `LICENSE` file at the
repository's root with the contents of an approved license that covers the
contents of the repository.

**[TOPLEVEL.README]** REQUIREMENT: There must be a markdown-formatted
`README.md` file at the repository's root that describes the library, explains how
to build it, and links to further documentation.

## `README.md`

**[README.TITLE]** RECOMMENDATION: The `README.md` should begin with a level 1
header with the name of the library optionally followed with a ":" and short
description.

For example:

```markdown
# beman.sender_receiver: Scalable Asychronous Program Building Blocks
```

**[README.PURPOSE]** RECOMMENDATION: Following the title, the `README.md` should
contain a one- or two-paragraph summary describing the library's purpose.

**[README.IMPLEMENTS]** RECOMMENDATION: Following the purpose and a newline, the
`README.md` should indicate which papers the repository implements. Use the following style:

```markdown
**Implements:** [`std::optional<T&>` (P2988R5)](https://wg21.link/P2988R5) and
[Give *std::optional* Range Support (P3168R1)](https://wg21.link/P3168R1).
```

## CMake

**[CMAKE.DEFAULT]** RECOMMENDATION: The root `CMakeLists.txt` should build all targets by default (including dependency targets).

**[CMAKE.PROJECT_NAME]** RECOMMENDATION: The CMake project name should be
identical to the beman library name.

**[CMAKE.LIBRARY_NAME]** RECOMMENDATION: The CMake library target's name should
be identical to the library name.

Example:

```CMake
add_library(beman.smart_pointer STATIC)
#...
```

**[CMAKE.LIBRARY_ALIAS]** REQUIREMENT: The CMake code must create an alias of
the library target named `beman::<short_name>`. This target is intended for
external use.

Example:

```CMake
add_library(beman::smart_pointer ALIAS beman.smart_pointer)
#...
```

**[CMAKE.TARGET_NAMES]** RECOMMENDATION: All targets, aside from the library
target, should begin with a `<library_name>.` prefix

```CMake
add_executable(beman.smart_pointer.examples.basic)
#...
add_executable(beman.smart_pointer.tests.roundtrip)
#...
```

**[CMAKE.CONFIG]** REQUIREMENT: At `install` time, a
`<library_name>Config.cmake` must be created which exports a
`beman::<short_name>` target.

**[CMAKE.SKIP_TESTS]** RECOMMENDATION: The root `CMakeLists.txt` should not build tests and their dependencies when `BUILD_TESTING` is set to `OFF` (see [CTest docs](https://cmake.org/cmake/help/latest/module/CTest.html)). Use the following style:

```CMake
# <repo>/CMakeLists.txt
# ...
if(BUILD_TESTING)
  FetchContent_Declare(
    googletest
    GIT_REPOSITORY https://github.com/google/googletest.git
    GIT_TAG f8d7d77c06936315286eb55f8de22cd23c188571 # release-1.14.0
  )
  FetchContent_MakeAvailable(googletest)
endif()

# ...
if(BUILD_TESTING)
  add_subdirectory(/path/to/tests)
endif()
```

**[CMAKE.AVOID_PASSTHROUGHS]** RECOMMENDATION: Avoid `CMakeLists.txt` files
consisting of a single `add_subdirectory` call.

In other words prefer,

```CMake
# <repo>/CMakeLists.txt
# ...
add_subdirectory(src/beman/optional26)
```

to,

```CMake
# <repo>/CMakeLists.txt
# ...
add_subdirectory(src) # Don't do this

# <repo>/src/CMakeLists.txt
add_subdirectory(beman) # Don't do this

# <repo>/src/beman/CMakeLists.txt
add_subdirectory(optional26) # Don't do this
```

## Directory Layout

**[DIRECTORY.INTERFACE_HEADERS]** REQUIREMENT: Header files that are part of the
public interface must reside within the `include/beman/<short_name>/`
directory.

**[DIRECTORY.IMPLEMENTATION_HEADERS]** REQUIREMENT: Header files residing within
`include/beman/<short_name>/` that are not part of the public interface
must either begin with `detail_` or reside within a subdirectory of
`include/beman/<short_name>/` called `detail` or begins with `detail_`.

**[DIRECTORY.SOURCES]** RECOMMENDATION: Sources and headers not part of the
public interface should reside in `src/`.

## C++

**[CPP.NAMESPACE]**: Headers in `include/beman/<short_name>/` should export
entities in the `beman::<short_name>` namespace.

## File contents

**[FILE.LICENSE_ID]** REQUIREMENT: The [SPDX license
identifier](https://spdx.dev/learn/handling-license-info/) must be added at the
first possible line in all files which can contain a comment 
(e.g., C++, scripts, CMake/Makefile, YAML/YML, JASON, XML, HTML, LaTeX, Dockerfile etc). 

Examples:
* C++ files shall use the following form:

```C++
// SPDX-License-Identifier: <SPDX License Expression>
```

* CMake files and scripts shall use the following form:

```CMake
# SPDX-License-Identifier: <SPDX License Expression>
```

* Markdown files will use a comment following the title:

```markdown
# Title

<!--
SPDX-License-Identifier: <SPDX License Expression>
-->
```

**[FILE.COPYRIGHT]** RECOMMENDATION: Source code files should NOT include a
copyright notice following the SPDX license identifier.
