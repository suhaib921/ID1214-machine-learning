A real-world example: Children diseases
Rubella is a contagious viral infection best known by its distinctive red rash.
It's also called German measles or three-day measles. This infection may cause
mild or no symptoms in most people. However, it can cause serious problems for
unborn babies whose mothers become infected during pregnancy.

https://www.youtube.com/watch?v=C-ZmfZNP5ns&t=401s

Rules

1. IF fever AND rash AND swollen_lymph_nodes THEN disease IS Rubella.
2. IF Rubella THEN recommend_vaccine IS MMR.
3. IF Rubella AND severe_rash THEN advise_medical_attention IS True.
4. IF fever AND rash AND conjunctivitis THEN disease IS Measles.
5. IF cough AND difficulty_breathing THEN disease IS Bronchitis.
6. IF fever AND sore_throat AND red_tonsils THEN disease IS Tonsillitis.
7. IF Rubella AND pregnant_woman THEN risk_category IS High.
8. IF Rubella AND vaccination_status IS Not_Vaccinated THEN recommend_vaccination IS True.
9. IF Rubella THEN advise_rest IS True.
10. IF Rubella THEN advise_hydration IS True.
11. IF child_is_underweight AND Rubella THEN recommend_dietary_support IS True.
12. IF child_has_fever THEN recommend_paracetamol IS True.
13. IF Rubella AND persistent_symptoms THEN recommend_further_tests IS True.
14. IF Rubella AND fever_above_38c THEN recommend_medical_consultation IS True.
15. IF Rubella THEN alert_health_authority IS True.
16. IF Rubella AND traveling_recently THEN check_contact_tracing IS True.
17. IF Rubella AND school_attendance THEN advise_school_absence IS True.
18. IF child_is_vaccinated THEN disease_likelihood IS Low.
19. IF fever AND rash AND swollen_lymph_nodes THEN recommend_lab_test IS Rubella_Test.
20. IF child_is_immunocompromised THEN recommend_additional_care IS True.



