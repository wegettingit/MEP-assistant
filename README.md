# 🧠 MEP Command Map (v1)

This doc outlines supported commands for the Mise en Place assistant AI.  
Each command is handled by a GPT logic layer or future API-to-database integration.

---

## 💬 Command Syntax

### `!assign [Name] [Task]`
Assigns a task to a staff member.  
Example:
```plaintext
!assign Frey restock veg bins
!status
Returns current active staff, urgent tasks, and completed items.

!911 or !86d
Flags an item or task as urgent or unavailable.
Example: !911 chicken thighs
!quote
Returns a motivational or philosophical quote for the shift.
Pulled from a rotating GPT list.
!inventory [item] [amount]
Updates the kitchen’s inventory count manually.
Example: !inventory eggs 6
🛠️ Planned Additions
!menu – pulls the daily menu for context-sensitive recommendations

!prepboard – returns outstanding prep

!shiftnotes – logs comments from staff or chefs

---

<!-- MEP Kitchen Assistant Embed -->
<iframe
  src="https://typebot.io/cmb086vjm001hpb8eqk7enlwhu"
  style="width:100%; height:600px; border:none;"
  allow="clipboard-write"
  title="Talk to MEP – Your Kitchen Assistant">
</iframe>

---
