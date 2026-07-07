<script>
  export let question = "";
</script>

<div class="question-input">
  <label for="question">Ask a Question</label>

  <textarea
    id="question"
    bind:value={question}
    placeholder="Ask a question about your project, architecture, codebase, or requirements..."
  />
</div>

<style>
  .question-input {
    margin-bottom: 24px;
  }

  label {
    display: block;
    margin-bottom: 10px;
    font-size: 15px;
    font-weight: 600;
    color: #334155;
  }

  textarea {
    width: 100%;
    min-height: 180px;
    padding: 16px;
    font-size: 16px;
    line-height: 1.6;
    border: 1px solid #d1d5db;
    border-radius: 12px;
    resize: vertical;
    outline: none;
    transition: all 0.2s ease;
    box-sizing: border-box;
  }

  textarea:focus {
    border-color: #2563eb;
    box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.15);
  }

  textarea::placeholder {
    color: #94a3b8;
  }
</style>
