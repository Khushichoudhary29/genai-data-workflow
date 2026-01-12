## BigQuery ML & GenAI Inference Alignment

This project is designed to align with BigQuery ML and Gemini-based inference workflows.

### Conceptual Flow
1. Customer review data is stored in a data warehouse (BigQuery).
2. BigQuery ML models or remote Gemini models can be referenced directly using SQL.
3. Text data (`reviewText`) is passed to a generative model for summarization and insight generation.
4. Generated insights can be stored back into BigQuery tables for downstream analytics or dashboards.

### Example BigQuery ML Workflow (Conceptual)

```sql
-- Reference a remote Gemini model
CREATE MODEL `project.dataset.gemini_model`
REMOTE WITH CONNECTION `project.region.connection`
OPTIONS (endpoint = 'gemini-pro');

-- Generate text insights
SELECT
  review_id,
  ML.GENERATE_TEXT(
    MODEL `project.dataset.gemini_model`,
    reviewText
  ) AS insights
FROM `project.dataset.reviews`;
