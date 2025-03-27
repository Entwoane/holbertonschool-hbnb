# HBNB ENTITY RELATIONSHIP DIAGRAM

  
*This diagram helps to visualize the relationships between tables inside the database.*

---


[![](https://mermaid.ink/img/pako:eNp9U1tv2jAU_iuWn2mUCwHqt5RmGhKFiTGmVZEiC5tgLbEj2xntAv-9znWhQ8QvOd_xd5GPTgn3glCIIJXPDCcSZxH_8T3cgPP54eFcgm_LYB4iIE5cDRqiBJtwtwh_InCSTNP_eqbYBdvFeoVAhn9X_VroM_mI-87lbFmdXxy8hKvF9tfVhVvakioq_1AS8ZZxT6Y6dcoy4sB886_BBjDSFLtgU9cHJpWOOc7oNZ7im3COlToJ2Yo8rdfLMFgBpmJMMmb8Ll36e56a6fSTLqFqL1mumeBN48tyHWxBLtmeDoEUG3JBrjHBkwFY65n5URlXxiZR8_r3I9E3PWhLY8OTAVCoVq5H8hTvaefQTeOeRfOYdZx-ojcJz8E2BEpjqWOCNR2AlJMW6t45vuX8L1oPGW_O9HuXF45gIhmBSMuCjmBGZYarEtYyEdRHasJCZH4JPeAi1RE0REPLMX8VIuuYUhTJEaIDTpWpirxK1-5Vf8WkpnIuCq4hcj3brUUgKuGbqaee5Y5t27WnvvPoe84IvkM0cSx_5tr-2PFmzszzH8eXEfxb29rWdGobaDzznIk_cWx_BClhWsiXZq_r9b58ANo9M5w?type=png)](https://mermaid.live/edit#pako:eNp9U1tv2jAU_iuWn2mUCwHqt5RmGhKFiTGmVZEiC5tgLbEj2xntAv-9znWhQ8QvOd_xd5GPTgn3glCIIJXPDCcSZxH_8T3cgPP54eFcgm_LYB4iIE5cDRqiBJtwtwh_InCSTNP_eqbYBdvFeoVAhn9X_VroM_mI-87lbFmdXxy8hKvF9tfVhVvakioq_1AS8ZZxT6Y6dcoy4sB886_BBjDSFLtgU9cHJpWOOc7oNZ7im3COlToJ2Yo8rdfLMFgBpmJMMmb8Ll36e56a6fSTLqFqL1mumeBN48tyHWxBLtmeDoEUG3JBrjHBkwFY65n5URlXxiZR8_r3I9E3PWhLY8OTAVCoVq5H8hTvaefQTeOeRfOYdZx-ojcJz8E2BEpjqWOCNR2AlJMW6t45vuX8L1oPGW_O9HuXF45gIhmBSMuCjmBGZYarEtYyEdRHasJCZH4JPeAi1RE0REPLMX8VIuuYUhTJEaIDTpWpirxK1-5Vf8WkpnIuCq4hcj3brUUgKuGbqaee5Y5t27WnvvPoe84IvkM0cSx_5tr-2PFmzszzH8eXEfxb29rWdGobaDzznIk_cWx_BClhWsiXZq_r9b58ANo9M5w)

---

## Relationships:

- *User* can own multiple *Places* and write multiple *Reviews* and make multiple *Reservations*
- *Place* belong to one *User*, can have multiple *Reviews* and multiple *Reservation* and is associated with multiple *Amenities* through the *Place_Amenity* table
- *Review* is written by one *User* about one *Place*
- *Amenity* can be associated  with multiple *Places* through the *Place_Amenity* table
- *Place_Amenity* represents the many to many relationship between *Place* and *Amenity*
