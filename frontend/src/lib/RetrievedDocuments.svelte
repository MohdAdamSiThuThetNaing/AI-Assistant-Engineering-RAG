<script>
  export let documents = [];
</script>

{#if documents.length}
  <div class="card">
    <div class="header">
      <h2>Retrieved Documents</h2>
      <span>{documents.length} found</span>
    </div>

    <div class="documents">
      {#each documents as doc}
        <div class="document">
          <div class="content">
            <div class="name">{doc}</div>

            <div class="description">
              Retrieved from the engineering knowledge base
            </div>
          </div>
        </div>
      {/each}
    </div>
  </div>
{/if}

<style>
  .card {
    margin-top: 32px;

    background: #fff;

    border: 1px solid #e5e7eb;

    border-radius: 18px;

    overflow: hidden;

    box-shadow:
      0 8px 24px rgba(15, 23, 42, 0.06),
      0 2px 6px rgba(15, 23, 42, 0.04);
  }

  .header {
    display: flex;

    justify-content: space-between;

    align-items: center;

    padding: 18px 24px;

    border-bottom: 1px solid #e5e7eb;

    background: #f8fafc;
  }

  .header h2 {
    margin: 0;

    font-size: 1.15rem;

    color: #111827;
  }

  .header span {
    padding: 6px 12px;

    border-radius: 999px;

    background: #dbeafe;

    color: #1d4ed8;

    font-size: 0.8rem;

    font-weight: 600;
  }

  .documents {
    padding: 20px;
  }

  .document {
    display: flex;

    align-items: flex-start;

    gap: 16px;

    padding: 18px;

    margin-bottom: 16px;

    border: 1px solid #e5e7eb;

    border-radius: 14px;

    transition: 0.2s;

    background: white;
  }

  .document:last-child {
    margin-bottom: 0;
  }

  .document:hover {
    background: #f8fafc;

    border-color: #93c5fd;

    transform: translateY(-2px);
  }

  .icon {
    width: 48px;

    height: 48px;

    display: flex;

    align-items: center;

    justify-content: center;

    border-radius: 12px;

    background: #eff6ff;

    font-size: 24px;
  }

  .content {
    flex: 1;
  }

  .name {
    font-weight: 700;

    color: #111827;

    margin-bottom: 6px;
  }

  .description {
    color: #64748b;

    font-size: 0.92rem;

    line-height: 1.6;
  }

  @media (max-width: 768px) {
    .header {
      flex-direction: column;

      align-items: flex-start;

      gap: 10px;
    }

    .document {
      padding: 14px;
    }
  }
</style>
