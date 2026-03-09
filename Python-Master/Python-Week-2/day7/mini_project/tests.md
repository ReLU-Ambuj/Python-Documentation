# Manual Test Cases

1. Add empty name (Should fail)
2. Add David with phone "123-ABC" (Should fail length/digit check constraint based on impl)
3. Add Sarah with email "sarah@com" (Should fail regex if strict enough, or pass if basic)
4. Add Alice, Bob, and Charlie.
5. Search "A" (Should return Alice)
6. Exit app. Change code. Run app. Are Alice, Bob, Charlie still there?
7. Delete Bob. View all. Bob should be gone.
