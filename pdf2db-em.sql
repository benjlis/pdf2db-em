-- name: dc19pdf-list
-- Get list of all pdfs that can be processed
select dc19_id, foiarchive_file from covid19.dc19_metadata
where ready;
