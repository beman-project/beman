# The Beman Standard

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

## Repository layout

## File contents
