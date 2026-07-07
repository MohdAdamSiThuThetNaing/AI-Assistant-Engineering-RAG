<script>
  import { createEventDispatcher } from "svelte";

  export let loading = false;
  export let disabled = false;

  const dispatch = createEventDispatcher();

  function handleClick() {
    dispatch("analyze");
  }
</script>

<button
  class="analyze-btn"
  on:click={handleClick}
  disabled={loading || disabled}
>
  {#if loading}
    Analyzing...
  {:else}
    Analyze
  {/if}
</button>

<style>
  .analyze-btn {
    width: 100%;
    margin-top: 20px;
    padding: 14px 20px;
    border: none;
    border-radius: 12px;
    background: #2563eb;
    color: white;
    font-size: 16px;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.2s ease;
  }

  .analyze-btn:hover:not(:disabled) {
    background: #1d4ed8;
  }

  .analyze-btn:disabled {
    background: #94a3b8;
    cursor: not-allowed;
  }
</style>
