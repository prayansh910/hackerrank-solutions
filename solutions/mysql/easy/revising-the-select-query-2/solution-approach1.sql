-- ──────────────────────────────────────────────────
-- Link        https://www.hackerrank.com/challenges/revising-the-select-query-2/problem?isFullScreen=true
-- Problem     Revising the Select Query II
-- Difficulty  Easy
-- Subdomain   Basic Select
-- Platform    HackerRank
-- Language    mysql
-- Status      Accepted
-- Submitted   2026-10-26, 11:25 p.m.
-- ──────────────────────────────────────────────────

SELECT NAME 
FROM CITY
WHERE POPULATION > 120000
AND COUNTRYCODE ='USA'
