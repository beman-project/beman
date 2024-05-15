# The Beman Standard

<!--
SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception

Copyright (c) 2024 David Sankel <dsankel@boost.org>
-->

This document specifies rules and recommendations for Beman project libraries.
Its goal is to create consistency that facilitates the evaluation of, and
contribution to Beman libraries.

## Introduction

### Core principles

This standards is driven by four core principles:

1. **[CORE.QUALITY] Highest quality**. Standards track libraries impact a
  countless number of engineers and, consequently, should be of the highest
  quality.
2. **[CORE.PRODUCTION_READY] Production-ready**. To get production feedback on a
  library, it needs to be ready for that kind of usage.
3. **[CORE.INDUSTRY_STANDARD] Industry standard technology**. Where there's
  industry consensus on best practices, we should take advantage. Innovation in
  tooling and style is not our purpose.
4. **[CORE.INCLUSIVE] Welcoming and inclusive community**. Broad, useful
  feedback necessitates an unobstructed path for using, reviewing, and
  contributing to Beman libraries. This principle encompasses ergonomics,
  cross-industry participation, and cultural accommodation.

### Changing this document

This is a living document that adapts to evolving best practices and community
needs. The process for making changes is as follows:

1. Create a [discourse topic](https://discourse.boost.org) detailing the change
   and how it aligns with the core principles.
2. After some community discussion, create a PR with the actual change on
   [GitHub](https://github.com/beman-project/beman) with a *leads question*
   label. The PR should also link to the discourse topic.
3. Continue discussions on the PR and discourse topic.
4. The leads make a decision based on the community feedback.

### Conventions

This standard consists of entries which include an all-caps, dot-separated
identifier which is used for referencing.

With the exception of the core principles, these entries are either rules or
recommendations.

* **Rules** must be followed in order to conform to this standard. These entries
  are prefixed by "RULE:".
* **Recommendations** should be followed in general, but specific circumstances
  may make this a less-than-ideal choice. Libraries not following a specific
  recommendation can still conform to this standard. These entries are prefixed
  by "RECOMMENDATION:".

## License

**[LICENSE.APPROVED]** REQUIREMENT: All Beman libraries must be licensed
under an approved license. These are:

1. [Boost Software License 1.0](https://www.boost.org/LICENSE_1_0.txt)
2. [Apache License v2.0 with LLVM Exceptions](https://llvm.org/LICENSE.txt)
3. [The MIT License](https://opensource.org/license/mit)

**[LICENSE.BOOST]** RECOMMENDATION: All Beman libraries should be licensed
under the [Boost Software License 1.0](https://www.boost.org/LICENSE_1_0.txt).

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

**[LIBRARY_NAMES]** REQUIREMENT: Beman libraries names begin with `Beman.`
followed by an UpperCamelCase short name.

Examples are Beman.SmartPointer and Beman.SenderReceiver.

**[REPOSITORY_NAME]** RECOMMENDATION: The repository should be named after the
library name excluding the `Beman.` prefix.

For example, a Beman.SmartPointer library's repository should be named
`SmartPointer`.

## Top-level

The top-level of a Beman library repository must consist of `CMakeLists.txt`,
`LICENSE.txt`, and `README.md** files.

**[TOPLEVEL.CMAKE]** REQUIREMENT: There must be a `CMakeLists.txt` at the repository's root
that builds and tests (via. CTest) the library.

**[TOPLEVEL.LICENSE]** REQUIREMENT: There must be a `LICENSE.txt` at the
repository's root with the contents of an approved license that covers the
contents of the repository.

**[TOPLEVEL.README]** REQUIREMENT: There must be a markdown-formatted
`LICENSE.md` at the repository's root that describes the library, explains how
to build it, and links to further documentation.

## `README.md`

**[README.TITLE]** RECOMMENDATION: The `README.md` should begin with a level 1
header with the name of the library optionally followed with a ":" and short
description.

For example:

```markdown
# Beman.SenderReceiver: Scalable Asychronous Program Building Blocks
```

**[README.PURPOSE]** RECOMMENDATION: Following the title, the `README.md` should
contain a one- or two-paragraph summary describing the library's purpose.

## Directory Layout

**[DIRECTORY.INTERFACE_HEADERS]** REQUIREMENT: Header files that are part of the
public interface must reside within the `include/Beman/\<ShortName\>/`
directory.

**[DIRECTORY.SOURCES]** RECOMMENDATION: Sources and headers not part of the
public interface should reside in `src/`.

## File contents

**[FILE.LICENSE_ID]** REQUIREMENT: The [SPDX license
identifier](https://spdx.dev/learn/handling-license-info/) must be added at the
first possible line in files which can contain a comment.

C++ files shall use the following form:

```C++
// SPDX-License-Identifier: <SPDX License Expression>
```

CMake files and scripts shall use the following form


```CMake
# SPDX-License-Identifier: <SPDX License Expression>
```

Markdown files will use a comment following the title:

```markdown
# Title

<!--
SPDX-License-Identifier: <SPDX License Expression>
-->
```

**[FILE.COPYRIGHT]** RECOMMENDATION: Source code files should include a
copyright notice following the SPDX license identifier.

```C++
// Copyright (c) 2024 Ron Howard <ron@boost.org>
```
