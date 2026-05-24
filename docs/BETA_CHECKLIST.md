# Private Beta Checklist

## Must work before first users

- Create a business profile
- Add customers from manual chat input
- Analyze new customer messages
- Save order details from a message
- Draft replies without auto-sending
- Track payment reminders
- Track follow-ups
- Show a daily action plan
- Export order rows
- Keep human approval before outbound messages

## Nice to have after first users

- WhatsApp adapter
- Persistent database storage
- Seller dashboard UI
- Basic auth and business access control
- Demo data reset button


## Database readiness

- Confirm `DATABASE_URL` is configured for the target environment.
- Run `/database/readiness` after deployment.
- Confirm backups and migration process before using real seller data.
