# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 0.1.x   | :white_check_mark: |

## Reporting a Vulnerability

If you discover a security vulnerability in ShopTalk, please **do not** open a public GitHub issue.

Instead, report it privately by opening a [GitHub Security Advisory](https://github.com/ShageeshanT/shoptalk/security/advisories/new).

Please include:

- A description of the vulnerability
- Steps to reproduce the issue
- The potential impact
- Any suggested fix (optional)

We aim to acknowledge reports within **48 hours** and provide a fix or mitigation within **14 days** for critical issues.

## Security Considerations

ShopTalk handles customer messages and order data. Key areas of concern:

- **API key exposure**: Never commit `.env` files. Use `.env.example` as a template.
- **SQL injection**: All database queries use parameterised SQLAlchemy expressions.
- **Input validation**: All incoming data is validated with Pydantic schemas before processing.
- **Authentication**: Seller endpoints should be protected with API key auth (Phase 2 milestone).
- **Data retention**: Customer message data should be handled in accordance with local privacy laws.

## Responsible Disclosure

We follow a responsible disclosure policy. Once a fix is released, we will credit the reporter (with their permission) in the release notes.
