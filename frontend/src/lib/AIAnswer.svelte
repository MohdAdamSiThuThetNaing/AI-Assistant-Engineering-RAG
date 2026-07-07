<script>
  export let answer = "";
</script>

{#if answer}
  <div class="card">
    <h2>AI Answer</h2>

    <div class="answer">
      {answer}
    </div>
  </div>
{/if}

<style>
  .card {
    margin-top: 32px;
    background: #ffffff;
    border: 1px solid #e5e7eb;
    border-radius: 18px;
    overflow: hidden;
    box-shadow:
      0 8px 24px rgba(15, 23, 42, 0.06),
      0 2px 6px rgba(15, 23, 42, 0.04);
  }

  h2 {
    margin: 0;
    padding: 18px 24px;
    font-size: 1.15rem;
    font-weight: 700;
    color: #111827;
    background: #f8fafc;
    border-bottom: 1px solid #e5e7eb;
  }

  .answer {
    padding: 24px;
    color: #374151;
    font-size: 15px;
    line-height: 1.9;
    white-space: pre-wrap;
    word-break: break-word;
    background: #ffffff;
  }

  .answer p {
    margin: 0 0 16px;
  }

  .answer code {
    padding: 2px 6px;
    border-radius: 6px;
    background: #eef2ff;
    color: #4338ca;
    font-family: "SFMono-Regular", Consolas, monospace;
    font-size: 14px;
  }

  .answer pre {
    margin: 18px 0;
    padding: 18px;
    overflow-x: auto;
    border-radius: 12px;
    background: #0f172a;
    color: #f8fafc;
    font-family: "SFMono-Regular", Consolas, monospace;
  }

  .answer ul,
  .answer ol {
    margin: 16px 0;
    padding-left: 24px;
  }

  .answer li {
    margin-bottom: 10px;
  }

  @media (max-width: 768px) {
    .card {
      border-radius: 14px;
    }

    h2 {
      padding: 16px 18px;
      font-size: 1rem;
    }

    .answer {
      padding: 18px;
      font-size: 14px;
    }
  }
</style>
