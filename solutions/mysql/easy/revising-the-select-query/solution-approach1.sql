-- ──────────────────────────────────────────────────
-- Link        https://www.hackerrank.com/challenges/revising-the-select-query/problem?isFullScreen=true
-- Problem     Revising the Select Query I
-- Difficulty  Easy
-- Subdomain   Basic Select
-- Platform    HackerRank
-- Language    mysql
-- Status      Accepted
-- Submitted   2026-10-26, 11:22 p.m.
-- ──────────────────────────────────────────────────

select * from CITY 
where POPULATION >100000
AND COUNTRYCODE = 'USA' ;
