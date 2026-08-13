# Git and release workflow

Use `main` as the single permanent integration branch. Use short-lived branches for substantive work and Conventional Commit prefixes when useful.

No tag is created merely to mark progress. A stable tag `vX.Y.Z` requires:

1. implemented Change Sets and passing deterministic validation;
2. representative behavioral evaluation;
3. a dated changelog section;
4. current, immutable MODA provenance;
5. a frozen content commit and accepted audit evidence;
6. resolved or explicitly accepted security, privacy, compatibility, migration, and recovery effects;
7. passing required remote checks on the target commit;
8. explicit human approval.

This connector cannot create an approved annotated release tag; provide an exact human handoff only after all gates pass.
