<script>
  export let loading = false;
</script>

{#if loading}
  <div class="loading">
    <div class="spinner"></div>
    <span>Analyzing with RAG...</span>
  </div>
{/if}

<style>
  .loading {
    margin: 30px 0;
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 12px;
    color: #475569;
    font-weight: 600;
  }

  .spinner {
    width: 22px;
    height: 22px;
    border: 3px solid #e2e8f0;
    border-top-color: #2563eb;
    border-radius: 50%;
    animation: spin 0.8s linear infinite;
  }

  @keyframes spin {
    to {
      transform: rotate(360deg);
    }
  }
</style>
