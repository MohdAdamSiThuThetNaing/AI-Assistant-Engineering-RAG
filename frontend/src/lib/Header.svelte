<script>
  export let title = "Engineering AI Assistant";
  export let subtitle = "Retrieval-Augmented Generation (RAG)";
</script>

<header class="header">
  <h1>{title}</h1>

  <p>{subtitle}</p>
</header>

<style>
  .header {
    text-align: center;
    margin-bottom: 32px;
  }

  h1 {
    margin: 0;
    font-size: 2.8rem;
    font-weight: 700;
    color: #111827;
  }

  p {
    margin-top: 12px;
    font-size: 1.1rem;
    color: #64748b;
  }

  @media (max-width: 768px) {
    h1 {
      font-size: 2rem;
    }

    p {
      font-size: 1rem;
    }
  }
</style>
