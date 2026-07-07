<script>
  import Header from "./lib/Header.svelte";
  import QuestionInput from "./lib/QuestionInput.svelte";
  import AnalyzeButton from "./lib/AnalyzeButton.svelte";
  import Loading from "./lib/Loading.svelte";
  import ErrorMessage from "./lib/ErrorMessage.svelte";
  import RetrievedDocuments from "./lib/RetrievedDocuments.svelte";
  import AIAnswer from "./lib/AIAnswer.svelte";
  import Footer from "./lib/Footer.svelte";

  import { analyze as analyzeApi } from "./services/api";

  let question = "";
  let loading = false;
  let error = "";
  let result = null;

  async function analyze() {
    if (!question.trim()) {
      error = "Please enter a question.";
      return;
    }

    loading = true;
    error = "";
    result = null;

    try {
      result = await analyzeApi(question);
    } catch (e) {
      error = e.message;
    } finally {
      loading = false;
    }
  }
</script>

<Header />

<QuestionInput bind:question />

<AnalyzeButton {loading} disabled={!question.trim()} on:analyze={analyze} />

<Loading {loading} />

<ErrorMessage {error} />

<RetrievedDocuments documents={result?.documents ?? []} />

<AIAnswer answer={result?.answer ?? ""} />

<Footer />
