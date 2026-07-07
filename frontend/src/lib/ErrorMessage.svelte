<script>
  export let error = "";
</script>

{#if error}
  <div class="error">
    ⚠ {error}
  </div>
{/if}

<style>
  .error {
    margin-top: 20px;
    padding: 16px;
    border-radius: 12px;
    background: #fef2f2;
    border: 1px solid #fecaca;
    color: #dc2626;
    font-weight: 600;
  }
</style>
