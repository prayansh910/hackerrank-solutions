-- ──────────────────────────────────────────────────
-- Link        https://www.hackerrank.com/challenges/japanese-cities-name/problem?isFullScreen=true
-- Problem     Japanese Cities' Names
-- Difficulty  Easy
-- Subdomain   Basic Select
-- Platform    HackerRank
-- Language    mysql
-- Status      Accepted
-- Submitted   2026-10-26, 11:33 p.m.
-- ──────────────────────────────────────────────────

SELECT NAME FROM CITY 
WHERE COUNTRYCODE = 'JPN'
