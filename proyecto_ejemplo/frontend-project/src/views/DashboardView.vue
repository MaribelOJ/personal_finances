<script setup >
    import FooterCom from '../components/Dashboard/FooterCom.vue';
    import Sidebar from '../components/Dashboard/Sidebar.vue';
    import Topbar from '../components/Dashboard/Topbar.vue';
    import UserProfile from '../components/Users/UserProfile.vue';
</script>

<template>
    <div id="wrapper">
        <Sidebar />

        <div id="content-wrapper" class="d-flex flex-column">
            <!-- Main Content -->
            <div id="content">
                <Topbar />
                <UserProfile />
            </div>
            <FooterCom />
        </div>
    </div>
</template>