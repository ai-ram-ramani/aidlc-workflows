# Frontend Code Summary

## Files
- `frontend/index.html` — Calculator HTML structure with semantic markup, ARIA labels, and data-testid attributes
- `frontend/style.css` — Minimal/clean theme with CSS Grid layout, light colors, responsive sizing
- `frontend/app.js` — Calculator state management, API calls via fetch, event listeners

## Key Features
- Configurable API_URL constant (set after first CDK deploy)
- Operator highlight state
- Decimal point handling (prevents duplicates)
- Floating point display rounding
- Error display with CSS class toggle
- All interactive elements have data-testid attributes for automation
